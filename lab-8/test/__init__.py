from connector.Connector import Connector
from tools.DBSkydivingTools import DBSkydivingTools
from tools.DBTools import DBTools
import threading

from twins.Employee import Employee
from twins.EquipmentRent import EquipmentRent
from twins.Profile import Profile
from structures.Table import Table

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

    # Check the lazy loading.
    # for profile in profiles:
    #     print(profile.rents)
    # for profile in profiles:
    #     print(profile)

    # Check updating for a parent.
    # first_person = profiles[0]
    # first_person.user_name = "NIKITA"
    # first_person.user_surname = "NE_NIKITA"
    # first_person.user_cash = 0
    # first_person.user_id = 100

    # Check updating for a child.
    # random_rent = rents[2]
    # random_rent.equipment_amount = 100
    # random_rent.rent_start = "2012-12-12"
    # random_rent.rent_end = "2012-12-11"
    # random_rent.rent_payment = 0

    # Depends on what I want from code: to change user_id only in one record or in every. If consider this case
    # than the ref from the parent class in object should be erased.
    # Due to constraint I can't assign value not in parent table.
    # random_rent.user_id = 18
    # random_rent.equipment_id = 40

    # What happens in the field of connected objects? Everything is cool, because of using lazy loading - updating
    # each time after the attribute was accessed.
    # for profile in profiles:
    #     print(profile.rents)

    # What happens if I try to assign values of the child table from the parent? Everything will work fine.
    # random_profile = profiles[14]
    # print(random_profile.rents)
    # random_profile.rents[0].user_id = 1
    # print(random_profile.rents)

    # Deleting records with bad override of __del__.
    # print(profiles[0])
    # del profiles[0]
    # print(profiles[0])

    # Let's implement new class inheriting list and try to override method remove there.
    # profiles_table = Table("profiles")
    # for profile in profiles_table:
    #     print(profile)
    # random_profile = profiles_table[4]
    # profiles_table.remove(random_profile)
    # print("After removing:")
    # for profile in profiles_table:
    #     print(profile)

    # Let's test greedy loading.
    query = "SELECT * FROM employees"
    cursor.execute(query)
    data = cursor.fetchall()
    employees = [Employee(**row) for row in data]
    for employee in employees:
        print(employee)

    cursor.close()
    connector_1.disconnect()
    # connector_2.disconnect()
