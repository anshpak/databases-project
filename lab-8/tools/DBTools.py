import mysql.connector
import pandas as pd

from errors.ColumnNameMismatch import ColumnNameMismatch
from errors.TableNameMismatch import TableNameMismatch


class BDTools:

    def __init__(self):
        self.connector = None

    # def init_connection(self, host, user, password, database):
    #     self.connector = self.Connector(host, user, password, database)
    #
    # class Connector:
    #     def __init__(self, host, user, password, database):
    #         self.host = host
    #         self.user = user
    #         self.password = password
    #         self.database = database
    #         self.connection = None
    #
    #     def connect(self, successful_report=False):
    #         try:
    #             self.connection = mysql.connector.connect(
    #                 host=self.host,
    #                 user=self.user,
    #                 password=self.password,
    #                 database=self.database
    #             )
    #             if successful_report:
    #                 print("Connection successful!")
    #         except mysql.connector.Error as e:
    #             print(f"Error: {e}")
    #
    #     def disconnect(self):
    #         if self.connection:
    #             self.connection.close()
    #
    # def _is_valid_table_name(self, table):
    #     cursor = self.connector.connection.cursor()
    #     cursor.execute("SHOW TABLES")
    #     tables = cursor.fetchall()
    #     tables = [table for tpl in tables for table in tpl]
    #     cursor.close()
    #     return table in tables
    #
    # @staticmethod
    # def _is_valid_df_table_name(df, column):
    #     columns = df.columns.tolist()
    #     return column in columns
    #
    # def get_list_data(self, table, return_none_if_fails=False):
    #     try:
    #         if self._is_valid_table_name(table):
    #             cursor = self.connector.connection.cursor()
    #             query = f"SELECT * FROM {table}"
    #             cursor.execute(query)
    #             data = cursor.fetchall()
    #             lists = [list(row) for row in data]
    #             cursor.close()
    #             return lists
    #         else:
    #             raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
    #     except TableNameMismatch as e:
    #         print(f"Error: {e}")
    #         if return_none_if_fails:
    #             return None
    #         else:
    #             return []
    #
    # def get_df_data(self, table, index_column,
    #                 return_df_if_index_column_fails=True,
    #                 return_none_if_table_or_index_fails=False):
    #     try:
    #         if self._is_valid_table_name(table):
    #             query = f"SELECT * FROM {table}"
    #             df = pd.read_sql_query(query, self.connector.connection)
    #             BDTools.set_primary_key_as_df_index(df, index_column)
    #             return df
    #         else:
    #             raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
    #     except (TableNameMismatch, ColumnNameMismatch) as e:
    #         print(f"Error: {e}")
    #         if isinstance(e, ColumnNameMismatch) and return_df_if_index_column_fails:
    #             return df
    #         else:
    #             if return_none_if_table_or_index_fails:
    #                 return None
    #             else:
    #                 return pd.DataFrame()
    #
    # @staticmethod
    # def set_primary_key_as_df_index(df, column):
    #     if BDTools._is_valid_df_table_name(df, column):
    #         df.set_index(column, inplace=True)
    #     else:
    #         raise ColumnNameMismatch(f"Passed column name \"{column}\" absent in table.")
