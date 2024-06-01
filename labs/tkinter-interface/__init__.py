import re

from connector.Connector import Connector
from tools.DBSkydivingTools import DBSkydivingTools
from tools.DBTools import DBTools
import threading
from twins.Employee import Employee
from twins.EquipmentRent import EquipmentRent
from twins.Profile import Profile
from structures.Table import Table
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector.pooling

# def func(event):
#     try:
#         connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#         connector.connect(successful_report=False)
#         cursor_1 = connector.connection.cursor()
#         to_update_id = tree.item(tree.selection()[0])["values"][0]
#         temp = event.widget.cget("text")
#         pattern = r'^[1-9][0-9]*$'
#         pattern_for_num = r'^\+?[0-9]+\.?[0-9]*$'
#         value = None
#         column_temp = None
#         if temp == "Update id":
#             value = id_var.get()
#             column_temp = "user_id"
#         elif temp == "Update name":
#             value = name_var.get()
#             column_temp = "user_name"
#         elif temp == "Update surname":
#             value = surname_var.get()
#             column_temp = "user_surname"
#         elif temp == "Update cash":
#             value = cash_var.get()
#             column_temp = "user_cash"
#         if re.match(pattern_for_num, value) is None and (column_temp == "user_name" or column_temp == "user_surname"):
#             update_command = f"UPDATE profiles SET {column_temp} = %s where user_id = %s"
#             params = (value, to_update_id)
#             cursor_1.execute(update_command, params)
#             connector.connection.commit()
#         elif re.match(pattern, value) is not None and (column_temp == "user_id" or column_temp == "user_cash"):
#             update_command = f"UPDATE profiles SET {column_temp} = %s where user_id = %s"
#             params = (value, to_update_id)
#             cursor_1.execute(update_command, params)
#             connector.connection.commit()
#         cursor_1.close()
#         connector.disconnect()
#     except Exception as e:
#         print(e)
#         messagebox.showerror("Error", "Wrong data type.")
#         event.widget.config(state="normal")
#
#
# def refresh():
#     tree.delete(*tree.get_children())
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     data_1 = DBTools.get_list_data(connector, "profiles")
#     cols = DBTools.get_column_names_as_list(connector, "profiles")
#     for row in data_1:
#         tree.insert("", "end", values=row)
#     connector.disconnect()
#
#
# def confirm_transaction():
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     DBSkydivingTools.give_user(connector, from_var.get(), whom_var.get(), value_var.get())
#     connector.disconnect()
#
#
# def delete_row():
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     to_delete_id = tree.item(tree.selection()[0])["values"][0]
#     DBTools.delete_one_from_table(connector, "profiles", to_delete_id)
#     connector.disconnect()
#
#
# def add_row():
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     if id_var.get() != '':
#         DBTools.insert_one_into_table(connector, "profiles", id_var.get(), name_var.get(), surname_var.get(),
#                                       cash_var.get())
#     else:
#         DBTools.insert_one_into_table(connector, "profiles", name_var.get(), surname_var.get(),
#                                       cash_var.get())
#     connector.disconnect()
#
#
# def update_row():
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     dialog = tk.Toplevel(main)
#     dialog.title("Update row")
#     dialog.geometry("400x200")
#     tk.Label(dialog, text="user_id", width=10).grid(row=3, column=0)
#     tk.Label(dialog, text="user_name", width=10).grid(row=4, column=0)
#     tk.Label(dialog, text="user_surname", width=10).grid(row=5, column=0)
#     tk.Label(dialog, text="user_cash", width=10).grid(row=6, column=0)
#     button_1_1 = tk.Button(dialog, text="Update id", name="user_id", width=15)
#     button_1_1.grid(row=3, column=2)
#     button_1_1.bind("<Button-1>", func)
#     button_2_1 = tk.Button(dialog, text="Update name", name="user_name", width=15)
#     button_2_1.grid(row=4, column=2)
#     button_2_1.bind("<Button-1>", func)
#     button_3_1 = tk.Button(dialog, text="Update surname", name="user_surname", width=15)
#     button_3_1.grid(row=5, column=2)
#     button_3_1.bind("<Button-1>", func)
#     button_4_1 = tk.Button(dialog, text="Update cash", name="user_cash", width=15)
#     button_4_1.grid(row=6, column=2)
#     button_4_1.bind("<Button-1>", func)
#     tk.Entry(dialog, textvariable=id_var).grid(row=3, column=1)
#     tk.Entry(dialog, textvariable=name_var).grid(row=4, column=1)
#     tk.Entry(dialog, textvariable=surname_var).grid(row=5, column=1)
#     tk.Entry(dialog, textvariable=cash_var).grid(row=6, column=1)
#     connector.disconnect()
#
#
# def upload_file():
#     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
#     connector.connect(successful_report=False)
#     file_path = filedialog.askopenfilename()
#     DBTools.import_from_csv(connector, "profiles", file_path)
#     connector.disconnect()
#
# if __name__ == "__main__":
    # main = tk.Tk()
    # main.geometry("800x600")
    # tree = ttk.Treeview()
    # tree.grid(row=0, column=0, columnspan=5)
    # data = DBTools.get_list_data(connector_1, "profiles")
    # columns = DBTools.get_column_names_as_list(connector_1, "profiles")
    # tree["columns"] = columns
    # tree["show"] = "headings"
    # for column in columns:
    #     tree.column(column, width=80)
    #     tree.heading(column, text=column)
    # for row in data:
    #     tree.insert("", "end", values=row)
    # tk.Label(main, text="user_id", width=10).grid(row=4, column=0)
    # tk.Label(main, text="user_name", width=10).grid(row=5, column=0)
    # tk.Label(main, text="user_surname", width=10).grid(row=6, column=0)
    # tk.Label(main, text="user_cash", width=10).grid(row=7, column=0)
    # id_var = tk.StringVar()
    # name_var = tk.StringVar()
    # surname_var = tk.StringVar()
    # cash_var = tk.StringVar()
    # button_1 = tk.Button(main, text="Update id", name="user_id", width=15)
    # button_1.grid(row=4, column=5)
    # button_1.bind("<Button-1>", func)
    # button_2 = tk.Button(main, text="Update name", name="user_name", width=15)
    # button_2.grid(row=5, column=5)
    # button_2.bind("<Button-1>", func)
    # button_3 = tk.Button(main, text="Update surname", name="user_surname", width=15)
    # button_3.grid(row=6, column=5)
    # button_3.bind("<Button-1>", func)
    # button_4 = tk.Button(main, text="Update cash", name="user_cash", width=15)
    # button_4.grid(row=7, column=5)
    # button_4.bind("<Button-1>", func)
    # tk.Button(main, text="Refresh", width=10, command=refresh).grid(row=4, column=6)
    # tk.Entry(textvariable=id_var).grid(row=4, column=2)
    # tk.Entry(textvariable=name_var).grid(row=5, column=2)
    # tk.Entry(textvariable=surname_var).grid(row=6, column=2)
    # tk.Entry(textvariable=cash_var).grid(row=7, column=2)
    #
    # tk.Label(main, text="Transaction:", width=10).grid(row=10, column=0)
    # tk.Label(main, text="From:", width=10).grid(row=10, column=1)
    # tk.Label(main, text="Whom:", width=10).grid(row=10, column=4)
    # tk.Label(main, text="Value:", width=10).grid(row=10, column=6)
    # from_var = tk.StringVar()
    # whom_var = tk.StringVar()
    # value_var = tk.StringVar()
    # tk.Entry(textvariable=from_var).grid(row=10, column=2)
    # tk.Entry(textvariable=whom_var).grid(row=10, column=5)
    # tk.Entry(textvariable=value_var).grid(row=10, column=7)
    # tk.Button(main, text="Confirm", width=10, command=confirm_transaction).grid(row=10, column=10)
    # tk.Button(main, text="Delete row", command=delete_row).grid(row=11, column=0)
    # tk.Button(main, text="Add row", command=add_row).grid(row=11, column=1)
    # tk.Button(main, text="Update row", command=update_row).grid(row=11, column=2)
    # tk.Button(main, text="Upload", command=upload_file).grid(row=11, column=3)
    # main.mainloop()
