from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from students import MaleStud, MilitaryService, Child, FemaleStud, Friendship
from db_access.db_utils import DBUtils
from datetime import date

if __name__ == '__main__':
    engine = create_engine('firebird+fdb://sysdba:12345678@localhost/C:/windows/system32/students.fbd')
    # engine = create_engine('mysql+Jaybird JCA/JDBC driver 4.0.28://sysdba:12345678@localhost/test_connection')
    # engine = create_engine('mysql+jaybird://sysdba:12345678@localhost/test_connection')
    Session = sessionmaker(bind=engine)
    cur_session = Session()

    male_students_query = DBUtils.get_entity_data(cur_session, MaleStud)
    new_male_stud = MaleStud(id=1, name='Kirill', group=5, course=2, birth_date=date(2000, 11, 21))
    cur_session.add(new_male_stud)
    for instance in male_students_query:
        print(instance)
    # conn = fdb.connect(dsn='C:/windows/system32/students.fbd', user='SYSDBA',
    #                    password='12345678')
    # cur = conn.cursor()

    male_students_query_received = False
    male_students_query = None
    key = True
    while key:
        key = input('Press "1" to show the data, \nPress "2" to add new object, \nPress "3" to remove object, '
                    '\nEnter "cansel" to cansel changes, \nEnter "commit" to commit changes, \nPress "q" to leave. '
                    '\nInput: ')
        if key == '1':
            while True:
                print('-' * 80)
                entity = input('Choose data to observe: \n1. Male students, \nPress "q" to leave. \nInput: ')
                if entity == '1':
                    print('-' * 80)
                    print('Male students:')
                    if not male_students_query_received:
                        male_students_query = DBUtils.get_entity_data(cur_session, MaleStud)
                        male_students_query_received = True
                    for instance in male_students_query:
                        print(instance)
                    break
                elif entity == 'q':
                    break
        elif key == '2':
            while True:
                print('-' * 80)
                entity = input('Choose a type of an object to add: \n1. Male students, \nPress "q" to leave. \nInput: ')
                if entity == '1':
                    print('-' * 80)
                    print('Adding a new student:')
                    id_ = input('Enter student id: ')
                    name = input('Enter student name: ')
                    surname = input('Enter student surname: ')
                    year = input('Enter student year of births: ')
                    month = input('Enter student month of birth: ')
                    day = input('Enter student day of birth: ')
                    course = input('Enter student course: ')
                    group = input('Enter student group: ')
                    photo = None
                    DBUtils.add_entity_instance(cur_session, MaleStud(id=id_, name=name, surname=surname, birth_date=date(int(year), int(month), int(day)), course=course, group=group))
                    break
                elif entity == 'q':
                    break
        elif key == '3':
            while True:
                print('-' * 80)
                choice = input('Choose a type of an object to remove: \n1. Male students, \nPress "q" to leave.\nInput: ')
                if choice == '1':
                    print('-' * 80)
                    id_ = input('Enter student\'s id: ')
                    DBUtils.remove_entity_instance(cur_session, male_students_query, MaleStud, id_)
                    break
                elif choice == 'q':
                    break
        elif key == 'cansel':
            while True:
                print('-' * 80)
                choice = input('Choose what to cansel: \n1. Everything, \n2. Last change, \nPress "q" to '
                               'leave.\nInput: ')
                if choice == '1':
                    cur_session.rollback()
                    break
                elif choice == '2':
                    DBUtils.undo_last_change(cur_session)
                    break
                elif choice == 'q':
                    break
        elif key == 'commit':
            cur_session.commit()
        elif key == 'q':
            cur_session.close()
            break
        else:
            key = True
        print('-' * 80)