from connector.Connector import Connector
from errors.TableNameMismatch import TableNameMismatch
from tools.DBTools import DBTools
from twins.Profile import Profile


class Table(list):
    def __init__(self, table):
        super().__init__()
        self.table_name = table
        connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
        connector.connect(successful_report=False)
        cursor = connector.connection.cursor(dictionary=True)
        try:
            if DBTools.is_valid_table_name(connector, table):
                if table == "profiles":
                    query = "SELECT * FROM profiles"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    profiles = [Profile(**row) for row in data]
                    self.clear()
                    for profile in profiles:
                        self.append(profile)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")
        finally:
            if connector.connection.is_connected():
                cursor.close()
                connector.connection.disconnect()

    def remove(self, item):
        connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
        connector.connect(successful_report=False)
        cursor = connector.connection.cursor(dictionary=True)
        if self.table_name == "profiles":
            query = f"DELETE FROM {self.table_name} WHERE user_id = {item.user_id}"
            cursor.execute(query)
            super().remove(item)
            connector.connection.commit()
        cursor.close()
        connector.connection.disconnect()
