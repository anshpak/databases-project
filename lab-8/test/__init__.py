from connector.Connector import Connector
from tools.DBSkydivingTools import DBSkydivingTools
from tools.DBTools import DBTools
import threading

from twins.EquipmentRent import EquipmentRent
from twins.Profile import Profile

if __name__ == "__main__":
    connector_1 = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    connector_1.connect(successful_report=False)
    # connector_2 = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 2)
    # connector_2.connect(successful_report=False)
    # thread_1 = threading.Thread(target=DBSkydivingTools.give_user, args=(connector_1, 2, 1, 100))
    # thread_2 = threading.Thread(target=DBSkydivingTools.give_user, args=(connector_2, 1, 2, 100))
    # thread_1.start()
    # thread_2.start()
    # thread_1.join()
    # thread_2.join()

    # twin-classes
    query = "SELECT * FROM profiles"
    cursor = connector_1.connection.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    profiles = [Profile(**row) for row in data]

    query = "SELECT * FROM equipment_rent"
    cursor.execute(query)
    data = cursor.fetchall()
    rents = [EquipmentRent(**row) for row in data]

    # check the lazy loading
    # for profile in profiles:
    #     print(profile.rents)
    # for profile in profiles:
    #     print(profile)

    # check updating for a parent
    # first_person = profiles[19]
    # first_person.user_name = "NIKITA"
    # first_person.user_surname = "NE_NIKITA"
    # first_person.user_cash = 0
    # first_person.user_id = 100

    # check updating for a child
    first_rent = rents[0]
    first_rent.equipment_amount = 100
    first_rent.rent_start = "2012-12-12"
    first_rent.rent_end = "2012-12-11"
    first_rent.rent_payment = 0

    cursor.close()
    connector_1.disconnect()
    # connector_2.disconnect()
