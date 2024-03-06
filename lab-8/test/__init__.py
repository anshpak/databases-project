from connector.Connector import Connector
from tools.DBTools import DBTools

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    connector.connect(successful_report=False)
    employees_data = DBTools.get_list_data(connector,"employees", return_none_if_fails=False)
    print(employees_data)
    # equipment_df = connector.get_df_data("equipment", "equipment_id",
    #                                      return_df_if_index_column_fails=True,
    #                                      return_none_if_table_or_index_fails=False)
    # print(equipment_df)
    DBTools.table_to_csv(connector, "employees", "../backups/")
    # DBTools.table_to_json(connector, "employees", "../backups/")
    DBTools.insert_one_into_table(connector, "employees", "Alex", "Kushnerow",
                                  "system-analyst", "+375446749823")
    connector.disconnect()
