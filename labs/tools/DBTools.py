import csv
import json

import pandas as pd

from errors.ColumnNameMismatch import ColumnNameMismatch
from errors.TableNameMismatch import TableNameMismatch
from io import BytesIO
from PIL import Image


class DBTools:
    @staticmethod
    def is_valid_table_name(connector, table_to_check):
        try:
            if not isinstance(table_to_check, str):
                raise Exception(f'Types mismatch, str class expected, but {type(table_to_check).__name__} type was '
                                'received.')
            cursor = connector.connection.cursor()
            cursor.execute('SHOW TABLES')
            tables = cursor.fetchall()
            cursor.close()
            return bool([table for tpl in tables for table in tpl if table == table_to_check])
        except Exception as e:
            print(f"Error: {e}")
            return False

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
            if DBTools.is_valid_table_name(connector, table):
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
            if DBTools.is_valid_table_name(connector, table):
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
            if DBTools.is_valid_table_name(connector, table):
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
            if DBTools.is_valid_table_name(connector, table):
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
    def get_column_names_as_list(connector, table):
        try:
            if DBTools.is_valid_table_name(connector, table):
                connector.connection.reset_session()
                cursor = connector.connection.cursor()
                query = f"SELECT * FROM {table} LIMIT 1"
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                cursor.fetchone()
                cursor.close()
                return columns
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
            if DBTools.is_valid_table_name(connector, table):
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
            if DBTools.is_valid_table_name(connector, table):
                if isinstance(index[0], tuple) or isinstance(index[0], list):
                    index = tuple(index[0])
                primary_key = DBTools._get_primary_key_name(connector, table)
                if len(index) == 1:
                    parametric_str = primary_key[0] + " = %s"
                else:
                    parametric_str = primary_key[0] + " = %s" + "".join(
                        [" AND " + key + " = %s" for key in primary_key[1:]])
                cursor = connector.connection.cursor()
                query = "SELECT * FROM " + table + " WHERE " + parametric_str
                cursor.execute(query, index)
                with open(f"../backups/buff.csv", "w") as f:
                    writer = csv.writer(f, lineterminator="\n")
                    writer.writerow((table,))
                    writer.writerow(cursor.fetchone())
                cursor.close()
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
    def undo_last_delete(connector):
        with open(f"../backups/buff.csv", "r") as f:
            reader = csv.reader(f)
            table = next(reader)
            for row in reader:
                DBTools.insert_one_into_table(connector, table[0], row)
        with open(f"../backups/buff.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow('')

    @staticmethod
    def delete_many_from_table(connector, table, indexes):
        try:
            if DBTools.is_valid_table_name(connector, table):
                for index in indexes:
                    DBTools.delete_one_from_table(connector, table, index)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def update_one_in_table(connector, table, data, *index):
        try:
            if DBTools.is_valid_table_name(connector, table):
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
    def import_from_csv(connector, table, path, filename=None):
        try:
            if DBTools.is_valid_table_name(connector, table):
                # with open(f"{path}{filename}.csv", "r") as f:
                with open(f"{path}", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        DBTools.insert_one_into_table(connector, table, row)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def import_from_json(connector, table, path, filename=None):
        try:
            if DBTools.is_valid_table_name(connector, table):
                # with open(f"{path}{filename}.json", "r") as f:
                with open(f"{path}", "r") as f:
                    data = json.load(f)
                    for row in data:
                        DBTools.insert_one_into_table(connector, table, row)
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def _bad_synch_with_csv(connector, table, path, filename):
        try:
            if DBTools.is_valid_table_name(connector, table):
                data_from_table = DBTools.get_list_data(connector, table)
                primary_key = DBTools._get_primary_key_name(connector, table)
                with open(f"{path}{filename}.csv", "r") as f:
                    reader = csv.reader(f)
                    counter = 0
                    deleted_rows = 0
                    for csv_row, table_row in zip(reader, data_from_table):
                        counter += 1
                        table_row = [str(data) for data in table_row]
                        if csv_row != table_row:
                            columns = DBTools._get_column_names_as_tuple(connector, table)

                            position = []
                            for column in columns:
                                if column in primary_key:
                                    position += [columns.index(column)]
                            keys = []
                            values = []
                            index_table = []
                            index_csv = []
                            for pos in range(len(csv_row)):
                                keys += [columns[pos]]
                                values += [csv_row[pos]]
                            for pos in range(len(csv_row)):
                                if pos in position:
                                    index_csv += [csv_row[pos]]
                            for pos in range(len(table_row)):
                                if pos in position:
                                    index_table += [table_row[pos]]
                            if index_csv != index_table:
                                DBTools.delete_one_from_table(connector, table, index_csv)
                                deleted_rows += 1
                            DBTools.update_one_in_table(connector, table, dict(zip(keys, values)), index_table)
                with open(f"{path}{filename}.csv", "r") as f:
                    reader = csv.reader(f)
                    for i in range(counter):
                        f.readline()

                    for row in reader:
                        DBTools.insert_one_into_table(connector, table, row)
                if len(data_from_table) > counter:
                    cursor = connector.connection.cursor()
                    query = f"""
                    DELETE FROM {table}
                    ORDER BY {primary_key[0]} DESC
                    LIMIT %s;
                    """
                    cursor.execute(query, (len(data_from_table) - counter - deleted_rows,))
                    connector.connection.commit()
                    cursor.close()
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def synch_with_csv(connector, table, path, filename):
        try:
            if DBTools.is_valid_table_name(connector, table):
                data_pool_from_table = DBTools.get_list_data(connector, table)
                columns = DBTools._get_column_names_as_tuple(connector, table)
                primary_key = DBTools._get_primary_key_name(connector, table)
                primary_key_position = []
                interacted_indexes = []
                for column in columns:
                    if column in primary_key:
                        primary_key_position += [columns.index(column)]
                row_pool_key = [[] for _ in range(len(data_pool_from_table))]
                counter = 0
                for row_pool in data_pool_from_table:
                    for index in primary_key_position:
                        row_pool_key[counter] += [str(row_pool[index])]
                        counter += 1
                with (open(f"{path}{filename}.csv", "r") as f):
                    reader = csv.reader(f)
                    for row in reader:
                        row_reader_key = []
                        for index in primary_key_position:
                            row_reader_key += [row[index]]
                        if row_reader_key in row_pool_key:
                            row_pool = [str(data) for data in data_pool_from_table[row_pool_key.index(row_reader_key)]]
                            if row != row_pool:
                                for pos in range(len(row)):
                                    keys = []
                                    values = []
                                    keys += [columns[pos]]
                                    values += [row[pos]]
                                DBTools.update_one_in_table(connector, table, dict(zip(keys, values)), row_reader_key)
                            interacted_indexes += [row_reader_key]
                        else:
                            values = []
                            for pos in range(len(row)):
                                values += [row[pos]]
                            DBTools.insert_one_into_table(connector, table, values)
                            interacted_indexes += [row_reader_key]
                    for key in row_pool_key:
                        if key not in interacted_indexes:
                            DBTools.delete_one_from_table(connector, table, key)
        except TableNameMismatch as e:
            print(f"Error: {e}")

    @staticmethod
    def synch_with_json(connector, table, path, filename):
        try:
            if DBTools.is_valid_table_name(connector, table):
                data_pool_from_table = DBTools.get_list_data(connector, table)
                columns = DBTools._get_column_names_as_tuple(connector, table)
                primary_key = DBTools._get_primary_key_name(connector, table)
                primary_key_position = []
                interacted_indexes = []
                for column in columns:
                    if column in primary_key:
                        primary_key_position += [columns.index(column)]
                row_pool_key = [[] for _ in range(len(data_pool_from_table))]
                counter = 0
                for row_pool in data_pool_from_table:
                    for index in primary_key_position:
                        row_pool_key[counter] += [str(row_pool[index])]
                        counter += 1
                with open(f"{path}{filename}.json", "r") as f:
                    reader = json.load(f)
                    for row in reader:
                        row_reader_key = []
                        for index in primary_key_position:
                            row_reader_key += [str(row[index])]
                        if row_reader_key in row_pool_key:
                            row_pool = [str(data) for data in data_pool_from_table[row_pool_key.index(row_reader_key)]]
                            if row != row_pool:
                                for pos in range(len(row)):
                                    keys = []
                                    values = []
                                    keys += [columns[pos]]
                                    values += [row[pos]]
                                DBTools.update_one_in_table(connector, table, dict(zip(keys, values)), row_reader_key)
                            interacted_indexes += [row_reader_key]
                        else:
                            values = []
                            for pos in range(len(row)):
                                values += [row[pos]]
                            DBTools.insert_one_into_table(connector, table, values)
                            interacted_indexes += [row_reader_key]
                    for key in row_pool_key:
                        if key not in interacted_indexes:
                            DBTools.delete_one_from_table(connector, table, key)
        except TableNameMismatch as e:
            print(f"Error: {e}")

    # To do: update method to work with composite primary key.
    @staticmethod
    def update_with_image_by_id(connector, table, column, where_to_put_id, pic):
        try:
            if DBTools.is_valid_table_name(connector, table):
                if DBTools._is_valid_column_name(connector, table, column):
                    primary_key = DBTools._get_primary_key_name(connector, table)
                    cursor = connector.connection.cursor()
                    query = f"UPDATE {table} SET {column} = %s WHERE {primary_key[0]} = {where_to_put_id}"
                    with open(pic, 'rb') as file:
                        binary_data = file.read()
                    cursor.execute(query, (binary_data,))
                    cursor.close()
                    connector.connection.commit()
                else:
                    raise ColumnNameMismatch(f"Passed column name \"{column}\" absent in table.")
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except (TableNameMismatch, ColumnNameMismatch) as e:
            print(f"Error: {e}")

    # To do: update method to work with composite primary key.
    @staticmethod
    def display_image_by_id(connector, table, column, where_to_get_id):
        try:
            if DBTools.is_valid_table_name(connector, table):
                if DBTools._is_valid_column_name(connector, table, column):
                    cursor = connector.connection.cursor()
                    primary_key = DBTools._get_primary_key_name(connector, table)
                    query = f"SELECT {column} FROM {table} WHERE {primary_key[0]} = %s"
                    cursor.execute(query, (where_to_get_id,))
                    data = cursor.fetchall()[0][0]
                    image_bytes = bytes(data)
                    image_stream = BytesIO(image_bytes)
                    img = Image.open(image_stream)
                    img.show()
                    cursor.close()
                else:
                    raise ColumnNameMismatch(f"Passed column name \"{column}\" absent in table.")
            else:
                raise TableNameMismatch(f"Passed table name \"{table}\" absent in database.")
        except (TableNameMismatch, ColumnNameMismatch) as e:
            print(f"Error: {e}")


