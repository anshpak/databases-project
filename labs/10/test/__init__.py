from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.skydiving import Employee, Contract, Parent, Child
from db_access.db_utils import DBUtils

# To do:
# 1. Normal data output.
# 2. Console clear.
# 3. Path to employee photo.
# 4. Add connected data.
# 5. Input check while adding a new entity.
# 6. An opportunity to leave while adding object.
# 7. Add an opportunity to send changes on the server.
# 8. Add an opportunity to remove objects with multiple primary keys.

# Conventions:
# 1. I always know the name of the primary key.

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/skydiving')
    Session = sessionmaker(bind=engine)
    cur_session = Session()

    employees_query_received = False
    employees_query = None
    key = True
    while key:
        key = input('Press "1" to show the data, \nPress "2" to add new object, \nPress "3" to remove object, '
                    '\nPress "q" to leave.\nInput: ')
        if key == '1':
            show_key = True
            while show_key:
                print('-' * 80)
                entity = input('Choose data to observe: \n1. Employees\nPress "q" to leave.\nInput: ')
                if entity == '1':
                    print('-' * 80)
                    print('Employees:')
                    if not employees_query_received:
                        employees_query = DBUtils.get_entity_data(cur_session, Employee)
                        employees_query_received = True
                    for instance in employees_query:
                        print(instance)
                    show_key = False
                elif entity == 'q':
                    break
        elif key == '2':
            add_key = True
            while add_key:
                print('-' * 80)
                entity = input('Choose a type of an object to add: \n1. Employees\nPress "q" to leave.\nInput: ')
                if entity == '1':
                    print('-' * 80)
                    print('Adding a new employee:')
                    id_ = input('Enter employee id: ')
                    name = input('Enter employee name: ')
                    surname = input('Enter employee surname: ')
                    position = input('Enter employee position: ')
                    contact_info = input('Enter employee phone number: ')
                    # photo = input('Add a path to employee photo: ')
                    photo = None
                    DBUtils.add_entity_instance(cur_session, Employee(id=id_, name=name, surname=surname, position=position, contact_info=contact_info, photo=photo))
                    add_key = False
                elif entity == 'q':
                    break
        elif key == '3':
            remove_key = True
            while remove_key:
                print('-' * 80)
                entity = input('Choose a type of an object to remove: \n1. Employees\nPress "q" to leave.\nInput: ')
                if entity == '1':
                    print('-' * 80)
                    id_ = input('Enter employee\'s id: ')
                    DBUtils.remove_entity_instance(cur_session, Employee, id_)
                    remove_key = False
                elif entity == 'q':
                    break
        elif key == 'q':
            break
        else:
            key = True
        print('-' * 80)
