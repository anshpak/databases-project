import pandas as pd

from connector.Connector import Connector
from tools.DBTools import DBTools

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "world", 1)
    connector.connect(successful_report=False)

    # 1. Get countries starting with letter A.
    country_df = DBTools.get_df_data(connector, "country", "Code")
    print(country_df.loc[country_df["Name"].str.match("A")])

    # 2. Get countries where russian language can be heard.
    country_language_df = DBTools.get_df_data(connector, "countrylanguage", "CountryCode")
    indexes_of_countries_who_may_speak_rus = country_language_df[country_language_df.Language == "Russian"].index
    print(country_df.loc[indexes_of_countries_who_may_speak_rus])

    # 3. Get countries in which average population doesn't exceed population in capital city.
    city_df = DBTools.get_df_data(connector, "city", "ID")
    capitals_df = city_df.merge(country_df.dropna(subset=["Capital"]).Capital,
                                left_index=True,
                                right_on="Capital")[["CountryCode", "Population"]]
    # without the next line somehow indexes in two dataframes are mixed
    capitals_and_their_countries_population_df = capitals_df.merge(country_df.dropna(subset=["Capital"]),
                                                                   left_on="CountryCode",
                                                                   right_index=True)[
        ["Name", "Population_x", "Population_y"]]
    average_country_population_df = pd.DataFrame(
        {"Average Population": capitals_and_their_countries_population_df.Population_y /
                               city_df.groupby(["CountryCode"]).size()})
    capitals_and_their_countries_population_df = capitals_and_their_countries_population_df.merge(
        average_country_population_df, left_index=True, right_index=True)
    print(capitals_and_their_countries_population_df[
              capitals_and_their_countries_population_df.Population_x >=
              capitals_and_their_countries_population_df["Average Population"]][["Name"]])

    # 4. Get amount of cities from each region of Asia.
    print(city_df.merge(country_df.loc[country_df.Region.str.contains("Asia")],
                        left_on="CountryCode", right_index=True).groupby(["Region"]).size())

    # 5. Get countries in which people who speak unofficial languages are more than average population in 5
    # top cities of those countries.
    countries_with_five_or_more_cities_df = (country_df.merge(city_df, left_index=True, right_on="CountryCode")
                                             .groupby(["CountryCode"]).size())
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df[countries_with_five_or_more_cities_df >= 5]
    countries_with_five_or_more_cities_df = country_df.loc[countries_with_five_or_more_cities_df.index][["Name", "Population"]]
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df.merge(city_df, left_index=True,
                                                                                        right_on="CountryCode")
    countries_with_five_or_more_cities_df = (countries_with_five_or_more_cities_df.groupby(["Name_x"])
                                             .apply(lambda x: x.sort_values(by="Population_y", ascending=False)))
    countries_with_five_or_more_cities_df.rename(columns={'Name_x': 'CountryName'}, inplace=True)
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df.groupby("CountryName").head(5)
    print(countries_with_five_or_more_cities_df.groupby("CountryName").sum().Population_y / 5)
    connector.disconnect()
