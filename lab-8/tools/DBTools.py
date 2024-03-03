import pandas as pd

from errors.ColumnNameMismatch import ColumnNameMismatch
from errors.TableNameMismatch import TableNameMismatch


class DBTools:
    @staticmethod
    def _is_valid_table_name(connector, table):
        cursor = connector.connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tables = [table for tpl in tables for table in tpl]
        cursor.close()
        return table in tables

    @staticmethod
    def _is_valid_df_table_name(df, column):
        columns = df.columns.tolist()
        return column in columns

    @staticmethod
    def get_list_data(connector, table, return_none_if_fails=False):
        try:
            if DBTools._is_valid_table_name(connector, table):
                cursor = connector.connection.cursor()
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                data = cursor.fetchall()
                lists = [list(row) for row in data]
                cursor.close()
                return lists
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")
            if return_none_if_fails:
                return None
            else:
                return []

    @staticmethod
    def get_df_data(connector, table, index_column,
                    return_df_if_index_column_fails=True,
                    return_none_if_table_or_index_fails=False):
        try:
            if DBTools._is_valid_table_name(connector, table):
                query = f"SELECT * FROM {table}"
                df = pd.read_sql_query(query, connector.connection)
                DBTools.set_primary_key_as_df_index(df, index_column)
                return df
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except (TableNameMismatch, ColumnNameMismatch) as e:
            print(f"Error: {e}")
            if isinstance(e, ColumnNameMismatch) and return_df_if_index_column_fails:
                return df
            else:
                if return_none_if_table_or_index_fails:
                    return None
                else:
                    return pd.DataFrame()

    @staticmethod
    def set_primary_key_as_df_index(df, column):
        if DBTools._is_valid_df_table_name(df, column):
            df.set_index(column, inplace=True)
        else:
            raise ColumnNameMismatch(f"Passed column name \"{column}\" absent in table.")