from connector.Connector import Connector

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving")
    connector.connect(successful_report=False)
    # employees_data = connector.get_list_data("employees", return_none_if_fails=False)
    # print(employees_data)
    equipment_df = connector.get_df_data("equipment", "equipment_id",
                                         return_df_if_index_column_fails=True,
                                         return_none_if_table_or_index_fails=False)
    print(equipment_df)
