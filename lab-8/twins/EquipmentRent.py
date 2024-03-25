class EquipmentRent:
    def __init__(self, rent_id, student_id, equipment_id, equipment_amount, rent_start, rent_end, rent_payment):
        self.rent_id = rent_id
        self.student_id = student_id
        self.equipment_id = equipment_id
        self.equipment_amount = equipment_amount
        self.rent_start = rent_start
        self.rent_end = rent_end
        self.rent_payment = rent_payment

    def __repr__(self):
        return str(self.__dict__)