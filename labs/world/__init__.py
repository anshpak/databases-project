import pandas as pd

from connector.Connector import Connector
from tools.DBTools import DBTools

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "world", 1)
    connector.connect(successful_report=False)

    # 1. Get countries starting with letter A.
    print("First query: ")
    country_df = DBTools.get_df_data(connector, "country", "Code")
    print(country_df.loc[country_df["Name"].str.match("A")])
    print("\n\n")

    # 2. Get countries where russian language can be heard.
    print("Second query: ")
    country_language_df = DBTools.get_df_data(connector, "countrylanguage", "CountryCode")
    indexes_of_countries_who_may_speak_rus = country_language_df[country_language_df.Language == "Russian"].index
    print(country_df.loc[indexes_of_countries_who_may_speak_rus])
    print("\n\n")

    # 3. Get countries in which average population doesn't exceed population in capital city.
    print("Third query: ")
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
    print("\n\n")

    # 4. Get amount of cities from each region of Asia.
    print("Fourth query: ")
    print(city_df.merge(country_df.loc[country_df.Region.str.contains("Asia")],
                        left_on="CountryCode", right_index=True).groupby(["Region"]).size())
    print("\n\n")

    # 5. Get countries in which people who speak unofficial languages are more than average population in 5
    # top cities of those countries.
    print("Fifth query: ")
    countries_with_five_or_more_cities_df = (country_df.merge(city_df, left_index=True, right_on="CountryCode")
                                             .groupby(["CountryCode"]).size())
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df[
        countries_with_five_or_more_cities_df >= 5]
    countries_with_five_or_more_cities_df = country_df.loc[countries_with_five_or_more_cities_df.index][
        ["Name", "Population"]]
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df.merge(city_df, left_index=True,
                                                                                        right_on="CountryCode")
    countries_with_five_or_more_cities_df = (countries_with_five_or_more_cities_df.groupby(["Name_x"])
                                             .apply(lambda x: x.sort_values(by="Population_y", ascending=False)))
    countries_with_five_or_more_cities_df.rename(columns={'Name_x': 'CountryName'}, inplace=True)
    countries_with_five_or_more_cities_df = countries_with_five_or_more_cities_df.groupby("CountryName").head(5)
    unofficial_languages_df = (country_language_df[country_language_df.IsOfficial == "F"][["Percentage"]]
                               .groupby(["CountryCode"]).sum())
    unofficial_languages_df = unofficial_languages_df.merge(country_df, left_index=True, right_index=True)[
        ["Population", "Percentage", "Name"]]
    unofficial_languages_df["Population"] = (unofficial_languages_df.Population *
                                             (unofficial_languages_df.Percentage / 100))
    unofficial_languages_df = unofficial_languages_df.merge(
        countries_with_five_or_more_cities_df.groupby("CountryName").sum().Population_y / 5,
        left_on="Name", right_index=True)
    unofficial_languages_df = \
        unofficial_languages_df.loc[unofficial_languages_df.Population > unofficial_languages_df.Population_y][["Name"]]
    print(', '.join(unofficial_languages_df["Name"]))
    print("\n\n")

    # Task 1.1.3: get all African languages, people who speak them are more than people who live in top
    # three european cities.
    print("Task 1.1.3: ")

    query = """
    SELECT res2.Language FROM
    (
        SELECT SUM(Population) as sum_res FROM
        (
            SELECT country.Code, country.Name, city.Population FROM country
            INNER JOIN city
            ON city.CountryCode = country.Code
            WHERE country.Region LIKE '%Europe'
            ORDER BY Population DESC LIMIT 3
        ) as three_top_cities
    ) as res1
    CROSS JOIN
    (
        SELECT african_languages.Language, SUM(african_languages.how_much_speak) as people_who_speak FROM
        (
            SELECT country.Code, countrylanguage.Language, country.Population * countrylanguage.Percentage / 100 as how_much_speak FROM country
            INNER JOIN countrylanguage
            ON countrylanguage.CountryCode = country.Code
            WHERE country.Region LIKE '%Africa'
        ) as african_languages
        GROUP BY african_languages.Language
    ) as res2
    WHERE res2.people_who_speak > res1.sum_res;
    """
    cursor = connector.connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    cursor.close()
    print("\n\n")

    print("Task 1.1.4: ")
    european_top_cities_pop_df = (city_df.merge(country_df.loc[country_df.Region.str.contains("Europe")],
                                                left_on="CountryCode", right_index=True)[["Population_x"]]
                                  .sort_values(by="Population_x", ascending=False).head(3)["Population_x"].sum())
    african_languages_df = country_language_df.merge(country_df.loc[country_df.Region
                                                     .str.contains("Africa")],
                                                     left_index=True, right_index=True)[["Language",
                                                                                         "Population", "Percentage"]]
    african_languages_df["Population"] = african_languages_df.Population * african_languages_df.Percentage / 100
    african_languages_df = african_languages_df.groupby(["Language"]).sum()
    print(african_languages_df.loc[african_languages_df.Population > european_top_cities_pop_df].index)
    print("\n\n")

    connector.disconnect()
