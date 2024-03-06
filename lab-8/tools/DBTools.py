import csv
import json

import pandas as pd

from errors.ColumnNameMismatch import ColumnNameMismatch
from errors.TableNameMismatch import TableNameMismatch

from csv import reader


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
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                data = cursor.fetchall()
                # lists = [list(row) for row in data]
                # lists = []
                # row = cursor.fetchone()
                # while row is not None:
                #     lists += list(row)
                #     row = cursor.fetchone()
                cursor.close()
                return data
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
                connector.connection.reset_session()
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

    @staticmethod
    def table_to_csv(connector, table, path):
        try:
            if DBTools._is_valid_table_name(connector, table):
                connector.connection.reset_session()
                data = DBTools.get_list_data(connector, table)
                with open(f"{path}{table}.csv", "w") as f:
                    writer = csv.writer(f, lineterminator="\n")
                    for tup in data:
                        writer.writerow(tup)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def table_to_json(connector, table, path):
        try:
            if DBTools._is_valid_table_name(connector, table):
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                json_data = json.dumps(cursor.fetchall())
                with open(f"{path}{table}.json", "w") as f:
                    f.write(json_data)
                cursor.close()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def get_column_names_as_tuple(connector, table):
        connector.connection.reset_session()
        cursor = connector.connection.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        columns = (column[0] for column in cursor.description)
        cursor.close()
        return columns

    @staticmethod
    def insert_one_into_table(connector, table, *args):
        try:
            if DBTools._is_valid_table_name(connector,table):
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                parameters = tuple(["%s" for _ in range(len(args) - 1)])
                query = f"INSERT INTO {table} () VALUES {parameters})"
                values = ("employees", "Alex", "Kushnerow", "system-analyst", "+375446749823")
                cursor.execute(query, values)
                cursor.close()
                connector.connection.commit()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")
