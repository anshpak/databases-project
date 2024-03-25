from connector.Connector import Connector
from twins.EquipmentRent import EquipmentRent


class Profile:
    def __init__(self, user_id=None, user_name=None, user_surname=None, user_cash=None):
        self.user_id = user_id,
        self.user_name = user_name,
        self.user_surname = user_surname,
        self.user_cash = user_cash
        self.rents = []

    def __getattr__(self, item):
        if item == "rents":
            connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
            cursor = connector.connection.cursor(dictionary=True)
            query = "SELECT * FROM equipment_rent WHERE user_id = %s"
            params = (self.user_id,)
            cursor.execute(query, params)
            res = cursor.fethall()
            self.rents = [EquipmentRent(**row) for row in res]
        return object.__getattribute__(self, item)
