from connection.Connector import Connector

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving")
    connector.connect(successful_report=False)
    # employees_data = connector.get_list_data("employees")
    # print(employees_data)
    equipment_df = connector.get_df_data("equipment", "equipment_id", return_df_if_index_column_fails=False)
    print(equipment_df)
