from connector.Connector import Connector


class Employee:
    def __init__(self, employee_id, employee_name, employee_surname, employee_position, contact_info):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_surname = employee_surname
        self.employee_position = employee_position
        self.contact_info = contact_info
        self.courses = None
        self.get_courses()

    def get_courses(self):
        connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
        connector.connect(successful_report=False)
        cursor = connector.connection.cursor()
        query = ("""SELECT courses.course_id, course_name, course_hours, course_jumps FROM
                (SELECT course_id FROM employees_and_courses WHERE employee_id = %s) as employee_and_his_courses
                INNER JOIN courses
                ON employee_and_his_courses.course_id = courses.course_id;""")
        params = (self.employee_id,)
        cursor.execute(query, params)
        self.courses = cursor.fetchall()
        cursor.close()
        connector.disconnect()

    def __repr__(self):
        return str(self.__dict__)
