from connector.Connector import Connector
from tools.DBTools import DBTools

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    connector.connect(successful_report=False)
    # employees_data = DBTools.get_list_data(connector,"employees", return_none_if_fails=False)
    # print(employees_data)
    # equipment_df = connector.get_df_data("equipment", "equipment_id",
    #                                      return_df_if_index_column_fails=True,
    #                                      return_none_if_table_or_index_fails=False)
    # print(equipment_df)
    # DBTools.table_to_csv(connector, "employees", "../backups/")
    # DBTools.table_to_json(connector, "employees", "../backups/")
    # DBTools.insert_one_into_table(connector, "test", 100, 1, 1., 1., 1., "CHAR(20)", "VARCHAR(20)", "TEXT",
    #                               "2023-03-09", "15:00:00", "2023-03-09 15:00:00", "2023-03-09 15:00:00", 1,
    #                               "X'62696E6172795F64617461'", "binary", "one,two", "one")

    # DBTools.update_one_in_table(connector, "test", {"data1": 200}, 2, 2)
    # DBTools.import_from_csv(connector, "employees", "../src/", "temp-data")
    # DBTools.import_from_json(connector, "employees", "../src/", "temp-data")
    DBTools.synch_with_csv(connector, "employees", "../backups/", "employees")
    connector.disconnect()
