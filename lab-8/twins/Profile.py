from connector.Connector import Connector
from twins.EquipmentRent import EquipmentRent


class Profile:
    def __init__(self, user_id=None, user_name=None, user_surname=None, user_cash=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_surname = user_surname
        self.user_cash = user_cash
        self.rents = []

    def __getattribute__(self, item):
        if item == "rents":
            connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
            connector.connect(successful_report=False)
            cursor = connector.connection.cursor(dictionary=True)
            query = "SELECT * FROM equipment_rent WHERE user_id = %s"
            params = (self.user_id,)
            cursor.execute(query, params)
            res = cursor.fetchall()
            self.rents = [EquipmentRent(**row) for row in res]
            cursor.close()
            connector.disconnect()
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
        connector.connect(successful_report=False)
        cursor = connector.connection.cursor()
        if key == "user_id":
            if not self.__dict__:
                self.__dict__[key] = value
            else:
                query = "UPDATE profiles SET user_id = %s WHERE user_id = %s"
                params = (value, self.user_id)
                cursor.execute(query, params)
                self.__dict__[key] = value
        elif key == "user_name":
            self.__dict__[key] = value
            query = "UPDATE profiles SET user_name = %s WHERE user_id = %s"
            params = (value, self.user_id)
            cursor.execute(query, params)
        elif key == "user_surname":
            self.__dict__[key] = value
            query = "UPDATE profiles SET user_surname = %s WHERE user_id = %s"
            params = (value, self.user_id)
            cursor.execute(query, params)
        elif key == "user_cash":
            self.__dict__[key] = value
            query = "UPDATE profiles SET user_cash = %s WHERE user_id = %s"
            params = (value, self.user_id)
            cursor.execute(query, params)
        else:
            self.__dict__[key] = value
        connector.connection.commit()
        cursor.close()
        connector.disconnect()

    def __repr__(self):
        return str(self.__dict__)

    # In this case the whole table will be deleted.
    # def __del__(self):
    #     connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    #     connector.connect(successful_report=False)
    #     cursor = connector.connection.cursor()
    #     query = "DELETE FROM profiles WHERE user_id = %s"
    #     params = (self.user_id,)
    #     cursor.execute(query, params)
    #     connector.connection.commit()
    #     cursor.close()
    #     connector.disconnect()
