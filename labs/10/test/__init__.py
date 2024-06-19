from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.skydiving import Employee
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
# 9. Add errors processing: when the id to remove is not found.
# 10. Conflicts processing for cancelling changes.
# 11. Move queries of data to DBUtils.

# Conventions:
# 1. I always know the name of the primary key.

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/skydiving')
    Session = sessionmaker(bind=engine)
    cur_session = Session()

    # employees_query_received = False
    # employees_query = None
    # key = True
    # while key:
    #     key = input('Press "1" to show the data, \nPress "2" to add new object, \nPress "3" to remove object, '
    #                 '\nEnter "cansel" to cansel changes, \nEnter "commit" to commit changes, \nPress "q" to leave. '
    #                 '\nInput: ')
    #     if key == '1':
    #         while True:
    #             print('-' * 80)
    #             entity = input('Choose data to observe: \n1. Employees, \nPress "q" to leave. \nInput: ')
    #             if entity == '1':
    #                 print('-' * 80)
    #                 print('Employees:')
    #                 if not employees_query_received:
    #                     employees_query = DBUtils.get_entity_data(cur_session, Employee)
    #                     employees_query_received = True
    #                 for instance in employees_query:
    #                     print(instance)
    #                 break
    #             elif entity == 'q':
    #                 break
    #     elif key == '2':
    #         while True:
    #             print('-' * 80)
    #             entity = input('Choose a type of an object to add: \n1. Employees, \nPress "q" to leave. \nInput: ')
    #             if entity == '1':
    #                 print('-' * 80)
    #                 print('Adding a new employee:')
    #                 id_ = input('Enter employee id: ')
    #                 name = input('Enter employee name: ')
    #                 surname = input('Enter employee surname: ')
    #                 position = input('Enter employee position: ')
    #                 contact_info = input('Enter employee phone number: ')
    #                 # photo = input('Add a path to employee photo: ')
    #                 photo = None
    #                 DBUtils.add_entity_instance(cur_session, Employee(id=id_, name=name, surname=surname, position=position, contact_info=contact_info, photo=photo))
    #                 break
    #             elif entity == 'q':
    #                 break
    #     elif key == '3':
    #         while True:
    #             print('-' * 80)
    #             choice = input('Choose a type of an object to remove: \n1. Employees, \nPress "q" to leave.\nInput: ')
    #             if choice == '1':
    #                 print('-' * 80)
    #                 id_ = input('Enter employee\'s id: ')
    #                 DBUtils.remove_entity_instance(cur_session, employees_query, Employee, id_)
    #                 break
    #             elif choice == 'q':
    #                 break
    #     elif key == 'cansel':
    #         while True:
    #             print('-' * 80)
    #             choice = input('Choose what to cansel: \n1. Everything, \n2. Last change, \nPress "q" to '
    #                            'leave.\nInput: ')
    #             if choice == '1':
    #                 cur_session.rollback()
    #                 break
    #             elif choice == '2':
    #                 DBUtils.undo_last_change(cur_session)
    #                 break
    #             elif choice == 'q':
    #                 break
    #     elif key == 'commit':
    #         cur_session.commit()
    #     elif key == 'q':
    #         cur_session.close()
    #         break
    #     else:
    #         key = True
    #     print('-' * 80)
