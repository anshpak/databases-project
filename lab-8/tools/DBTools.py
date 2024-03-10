import csv
import json

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
    def _is_valid_column_name(connector, table, column):
        columns = DBTools._get_column_names_as_tuple(connector, table)
        return column in columns

    @staticmethod
    def _is_valid_df_column_name(df, column):
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
        if DBTools._is_valid_df_column_name(df, column):
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
    def _get_column_names_as_tuple(connector, table):
        connector.connection.reset_session()
        cursor = connector.connection.cursor()
        query = f"SELECT * FROM {table} LIMIT 1"
        cursor.execute(query)
        columns = tuple([column[0] for column in cursor.description])
        cursor.fetchone()
        cursor.close()
        return columns

    @staticmethod
    def _get_column_names_as_string(connector, table):
        connector.connection.reset_session()
        cursor = connector.connection.cursor()
        query = f"SELECT * FROM {table} LIMIT 1"
        cursor.execute(query)
        columns = ", ".join([column[0] for column in cursor.description])
        cursor.fetchone()
        cursor.close()
        return columns

    @staticmethod
    def _get_primary_key_name(connector, table):
        connector.connection.reset_session()
        cursor = connector.connection.cursor()
        command = f"SHOW KEYS FROM {table} WHERE KEY_NAME = 'PRIMARY'"
        cursor.execute(command)
        keys = cursor.fetchall()
        cursor.close()
        return [key[4] for key in keys]

    @staticmethod
    def _get_auto_increment_column(connector, table):
        cursor = connector.connection.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        columns_info = cursor.fetchall()
        cursor.close()
        res = ""
        for info in columns_info:
            if info[5] == "auto_increment":
                res = info[0]
        return res

    @staticmethod
    def insert_one_into_table(connector, table, *args):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = tuple(args[0])
        try:
            if DBTools._is_valid_table_name(connector, table):
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                parameters = ", ".join(["%s" for _ in range(len(args))])
                columns = DBTools._get_column_names_as_tuple(connector, table)
                if len(columns) == len(args):
                    columns = DBTools._get_column_names_as_string(connector, table)
                    query = f"INSERT INTO {table} (" + columns + ") VALUES (" + parameters + ")"
                    cursor.execute(query, args)
                else:
                    auto_incremented_column = DBTools._get_auto_increment_column(connector, table)
                    columns = ", ".join([column for column in columns if column != auto_incremented_column])
                    query = f"INSERT INTO {table} (" + columns + ") VALUES (" + parameters + ")"
                    cursor.execute(query, args)
                cursor.close()
                connector.connection.commit()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def delete_one_from_table(connector, table, *index):
        try:
            if DBTools._is_valid_table_name(connector, table):
                if isinstance(index[0], tuple) or isinstance(index[0], list):
                    index = index[0]
                primary_key = DBTools._get_primary_key_name(connector, table)
                if len(index) == 1:
                    parametric_str = primary_key[0]
                else:
                    parametric_str = primary_key[0] + " = %s" + "".join([" AND " + key + " = %s" for key in primary_key[1:]])
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                query = "DELETE FROM " + table + " WHERE " + parametric_str
                cursor.execute(query, index)
                cursor.close()
                connector.connection.commit()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def delete_many_from_table(connector, table, indexes):
        try:
            if DBTools._is_valid_table_name(connector, table):
                for index in indexes:
                    DBTools.delete_one_from_table(connector, table, index)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def update_one_in_table(connector, table, data, *index):
        try:
            if DBTools._is_valid_table_name(connector, table):
                if isinstance(index[0], tuple) or isinstance(index[0], list):
                    index = tuple(index[0])
                for column in data:
                    if not DBTools._is_valid_column_name(connector, table, column):
                        raise ColumnNameMismatch(f"Passed column name \"{column}\" absent in table.")
                parametric_str1 = ", ".join([column + " = %s" for column in data])
                primary_key = DBTools._get_primary_key_name(connector, table)
                if len(index) == 1:
                    parametric_str2 = primary_key[0] + " = %s"
                else:
                    parametric_str2 = primary_key[0] + " = %s" + "".join(
                        [" AND " + key + " = %s" for key in primary_key[1:]])
                data_and_index = tuple(data.values()) + index
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                query = f"UPDATE {table} SET {parametric_str1} WHERE {parametric_str2}"
                cursor.execute(query, data_and_index)
                connector.connection.commit()
                cursor.close()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except (TableNameMismatch, ColumnNameMismatch) as e:
            print(f"Error: {e}")

    @staticmethod
    def import_from_csv(connector, table, path, filename):
        try:
            if DBTools._is_valid_table_name(connector, table):
                with open(f"{path}{filename}.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        DBTools.insert_one_into_table(connector, table, row)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def import_from_json(connector, table, path, filename):
        try:
            if DBTools._is_valid_table_name(connector, table):
                with open(f"{path}{filename}.json", "r") as f:
                    data = json.load(f)
                    for row in data:
                        DBTools.insert_one_into_table(connector, table, row)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def synch_with_csv(connector, table, path, filename):
        try:
            if DBTools._is_valid_table_name(connector, table):
                data_from_table = DBTools.get_list_data(connector, table)
                with open(f"{path}{filename}.csv", "r") as f:
                    reader = csv.reader(f)
                    counter = 0
                    for csv_row, table_row in zip(reader, data_from_table):
                        counter += 1
                        table_row = [str(data) for data in table_row]
                        if csv_row != table_row:
                            columns = DBTools._get_column_names_as_tuple(connector, table)
                            primary_key = DBTools._get_primary_key_name(connector, table)
                            position = []
                            for column in columns:
                                if column in primary_key:
                                    position += [columns.index(column)]
                            keys = []
                            values = []
                            index = []
                            for pos in range(len(csv_row)):
                                if pos not in position:
                                    keys += [columns[pos]]
                                    values += [csv_row[pos]]
                                else:
                                    index += csv_row[pos]
                            DBTools.update_one_in_table(connector, table, dict(zip(keys, values)), index)
                with open(f"{path}{filename}.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        counter += 1
                        DBTools.insert_one_into_table(connector, table, row)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except Exception as e:
            print(f"Error: {e}")
