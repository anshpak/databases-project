import mysql.connector
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sic mundus creatus est',
            database='skydiving'
        )
        print("Connection successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM students")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # cursor.execute("SELECT equipment_condition, SUM(available_equipment_amount) FROM equipment GROUP BY equipment_condition")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # query = """SELECT student_id, student_first_name, student_second_name FROM students
    #     INNER JOIN cources
    #     ON students.cource_id = cources.cource_id
    #     WHERE cources.cource_name = 'Basic Freefall Skills'"""
    # cursor.execute(query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # query = """INSERT INTO students
    # (cource_id, student_first_name, student_second_name, student_birthday, student_sex,
    # student_contact_info, student_level, enrollment_date, completion_date, status)
    # VALUES
    # (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    # """
    # new_student = (1, 'Eugine', 'Bobus', '1998-03-14', 'male', '+375335783850', 'intermediate', '2023-06-21', '2023-11-11', 'closed')
    # cursor.execute(query, new_student)
    # connection.commit()
    # if cursor.rowcount > 0:
    #     print("New record was successfully added!")
    # else:
    #     print("New record wasn't added.")

    # query = """UPDATE students
    # SET
    # student_first_name = %s,
    # student_second_name = %s
    # WHERE student_id = %s"""
    # new_student_data = ('Andrey', 'Shpak', 106)
    # cursor.execute(query, new_student_data)
    # connection.commit()
    # if cursor.rowcount > 0:
    #     print("Record was successfully updated!")
    # else:
    #     print("Record wasn't updated.")

    # query = """DELETE FROM students WHERE student_id = %s"""
    # data_to_remove = 106
    # cursor.execute(query, (data_to_remove,))
    # connection.commit()
    # if cursor.rowcount > 0:
    #     print("Record was successfully removed!")
    # else:
    #     print("Record wasn't removed.")

    query = "SELECT * FROM students"
    index_col = 'student_id'
    df = pd.read_sql_query(query, connection, index_col=index_col)
    df.reset_index(drop=True, inplace=True)

    current_date = datetime.now()
    df['student_birthday'] = pd.to_datetime(df['student_birthday'])
    # print(df['student_birthday'].dtype)
    print((current_date - df['student_birthday']).dt.total_seconds() / (24 * 60 * 60))


    cursor.close()
    connection.close()
