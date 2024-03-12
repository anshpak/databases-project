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
        group_id = student_groups_df.loc[student_groups_df.group_name == group].index
        print(group_id)
        students_and_groups_df = students_df.groupby("group_id").size()
        return students_and_groups_df.loc[students_and_groups_df.group_id == group_id]

    @staticmethod
    def filter_equipment_by_condition(equipment_df, condition):
        filtered_equipment_df = equipment_df[equipment_df["equipment_condition"] == condition]
        return filtered_equipment_df

    @staticmethod
    def count_equipment_by_condition(equipment_df, condition):
        filtered_equipment_df = equipment_df.groupby("equipment_condition").sum()
        return filtered_equipment_df.loc[filtered_equipment_df.index == condition][["available_equipment_amount"]]
