from connector.Connector import Connector


class EquipmentRent:
    def __init__(self, rent_id, user_id, equipment_id, equipment_amount, rent_start, rent_end, rent_payment):
        self.rent_id = rent_id
        self.user_id = user_id
        self.equipment_id = equipment_id
        self.equipment_amount = equipment_amount
        self.rent_start = rent_start
        self.rent_end = rent_end
        self.rent_payment = rent_payment

    def __setattr__(self, key, value):
        connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
        connector.connect()
        cursor = connector.connection.cursor()
        if key == "rent_id":
            if not self.__dict__:
                self.__dict__[key] = value
            else:
                query = "UPDATE equipment_rent SET rent_id = %s WHERE rent_id = %s"
                params = (value, self.rent_id)
                cursor.execute(query, params)
                self.__dict__[key] = value
        elif key == "user_id":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET user_id = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        elif key == "equipment_id":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET equipment_id = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        elif key == "equipment_amount":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET equipment_amount = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        elif key == "rent_start":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET rent_start = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        elif key == "rent_end":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET rent_end = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        elif key == "rent_payment":
            self.__dict__[key] = value
            query = "UPDATE equipment_rent SET rent_payment = %s WHERE rent_id = %s"
            params = (value, self.rent_id)
            cursor.execute(query, params)
        connector.connection.commit()
        cursor.close()
        connector.disconnect()

    def __repr__(self):
        return str(self.__dict__)
