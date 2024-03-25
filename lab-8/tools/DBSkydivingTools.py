class DBSkydivingTools:
    @staticmethod
    def filter_students_by_level(students_df, level):
        filtered_students = students_df[students_df['student_level'] == level]
        return filtered_students

    @staticmethod
    def get_employee_contracts_info(employees_df, contracts_df):
        return employees_df.merge(contracts_df, left_index=True, right_index=True)[["employee_name",
                                                                                    "employee_surname",
                                                                                    "contract_start_date",
                                                                                    "contract_end_date",
                                                                                    "employee_salary"]]

    @staticmethod
    def count_students_in_group(student_groups_df, students_df, group):
        group_id = student_groups_df.loc[student_groups_df.group_name == group].index[0]
        students_and_groups_df = students_df.groupby("group_id").size()
        return students_and_groups_df[group_id]

    @staticmethod
    def filter_equipment_by_condition(equipment_df, condition):
        filtered_equipment_df = equipment_df[equipment_df["equipment_condition"] == condition]
        return filtered_equipment_df

    @staticmethod
    def count_equipment_by_condition(equipment_df, condition):
        filtered_equipment_df = equipment_df.groupby("equipment_condition").sum()
        return filtered_equipment_df.loc[filtered_equipment_df.index == condition][["available_equipment_amount"]]

    @staticmethod
    def give_user(connector, from_id, whom_id, value):
        try:
            with connector.connection.cursor() as cursor:
                query = f"SELECT * FROM ACCOUNTS WHERE user_id = %s OR user_id = %s"
                cursor.execute(query, (from_id, whom_id))
                cursor.fetchall()
                rows = cursor.rowcount
                if rows == 2:
                    with connector.connection.cursor() as cursor:
                        query = "UPDATE accounts SET user_cash = user_cash - %s WHERE user_id = %s"
                        cursor.execute(query, (value, from_id))
                        if cursor.rowcount == 1:
                            input()
                            query = "UPDATE accounts SET user_cash = user_cash + %s WHERE user_id = %s"
                            cursor.execute(query, (value, whom_id))
                            if cursor.rowcount == 1:
                                connector.connection.commit()
                            else:
                                connector.connection.rollback()
                        else:
                            connector.connection.rollback()
        except Exception as e:
            print(e)
            connector.connection.rollback()
