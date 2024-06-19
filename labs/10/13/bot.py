import json

import telebot
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from telebot import types
import requests

from db_access.db_utils import DBUtils
from models.skydiving import Employee
from models.user import User

service_URL = 'http://127.0.0.1:5000'
global cur_id
global temp_data_dict
global cur_user

bot = telebot.TeleBot('')

users_engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/users')
Session = sessionmaker(bind=users_engine)
cur_users_session = Session()


@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['Log in', 'Sign in', 'Exit']
    keyboard.add(*buttons)
    inner_message = bot.send_message(message.chat.id, 'Please, select an option:', reply_markup=keyboard)
    bot.register_next_step_handler(inner_message, provide_entry_actions)


def provide_entry_actions(message: types.Message):
    if message.text == 'Log in':
        user_login_message = bot.send_message(message.chat.id, 'Enter your login:',
                                              reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(user_login_message, check_login)
    elif message.text == 'Sign in':
        user_login_message = bot.send_message(message.chat.id, 'Enter your login:',
                                              reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(user_login_message, get_new_password)
    elif message.text == 'Exit':
        bot.send_message(message.chat.id, 'Type /start anytime you would like to start again',
                         reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a valid option')
        bot.register_next_step_handler(message, provide_entry_actions)


def get_new_password(message: types.Message):
    login = message.text
    user_password_message = bot.send_message(message.chat.id, 'Enter your password:')
    bot.register_next_step_handler(user_password_message, add_new_user, login)


def add_new_user(message: types.Message, login: str):
    DBUtils.add_entity_instance(cur_users_session, User(login=login, password=message.text, role='user'))
    cur_users_session.commit()


def check_login(message: types.Message):
    users_query = DBUtils.get_entity_data(cur_users_session, User)
    for instance in users_query:
        if instance.login == message.text:
            user_password_message = bot.send_message(message.chat.id, 'Enter your password:')
            bot.register_next_step_handler(user_password_message, check_password)
            return
    user_login_message = bot.send_message(message.chat.id, 'Error: incorrect login. Enter your login again')
    bot.register_next_step_handler(user_login_message, check_login)


def check_password(message: types.Message):
    users_query = DBUtils.get_entity_data(cur_users_session, User)
    for instance in users_query:
        if instance.password == message.text:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            buttons = ['Yes', 'No']
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Logged in. Congrats!')
            bot.send_message(message.chat.id, 'Hello! Should we start a work?', reply_markup=keyboard)
            global cur_user
            cur_user = instance
            bot.register_next_step_handler(message, show_menu)
            return
    user_password_message = bot.send_message(message.chat.id, 'Error: incorrect password. Enter your password again:')
    bot.register_next_step_handler(user_password_message, check_password)


def show_menu(message: types.Message):
    if message.text == 'Yes':
        global cur_user
        if cur_user.role == 'admin':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            buttons = ['Employees']
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Choose an entity to manage:', reply_markup=keyboard)
            bot.register_next_step_handler(message, show_data)
    elif message.text == 'No':
        cmd_start(message)
    else:
        bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a valid option')
        bot.register_next_step_handler(message, show_menu)


def show_data(message: types.Message):
    if message.text == 'Employees':
        response_result = requests.get(service_URL + '/employees')
        dict_from_server = pretty_string(response_result.json())
        bot.send_message(message.chat.id, dict_from_server, parse_mode='Markdown')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        buttons = ['Add a new one', 'Edit', 'Remove', 'Back to entities', 'Log out']
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Please, select an option:', reply_markup=keyboard)
        bot.register_next_step_handler(message, perform_actions_with_instance, 'Employee')
    else:
        bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a valid option')
        bot.register_next_step_handler(message, show_data)


def pretty_string(data: list):
    res = ""
    count = 1
    for elem in data:
        res += str(count) + "\n"
        res += "-" * 30 + "\n"
        for k, v in elem.items():
            res += " " * 10 + "*" + str(k) + "*" + ": " + "_" + str(v) + "_" + "\n"
        res += "-" * 30 + "\n"
        count += 1
    return res


def get_new_entity_instance_name(message: types.Message, entity_name):
    global temp_data_dict
    temp_data_dict = {}
    if entity_name == 'Employee':
        identifier = 'id'
        name = 'name'
    else:
        pass
    temp_data_dict[identifier] = message.text
    new_instance_id_message = bot.send_message(message.chat.id, 'Please, type a new ' + name + ':',
                                               reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(new_instance_id_message, get_new_entity_instance_surname, name, entity_name)


def get_new_entity_instance_surname(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        surname = 'surname'
    else:
        pass
    new_instance_name_message = bot.send_message(message.chat.id, 'Please, type a new ' + surname + ':',
                                                 reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(new_instance_name_message, get_new_entity_instance_position, surname, entity_name)


def get_new_entity_instance_position(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        position = 'position'
    else:
        pass
    new_instance_surname_message = bot.send_message(message.chat.id, 'Please, type a new ' + position + ':',
                                                    reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(new_instance_surname_message, get_new_entity_instance_contact_info, position,
                                   entity_name)


def get_new_entity_instance_contact_info(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        contact_info = 'contact_info'
    else:
        pass
    new_instance_position_message = bot.send_message(message.chat.id, 'Please, type a new a new phone number:',
                                                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(new_instance_position_message, get_new_entity_instance_photo, contact_info,
                                   entity_name)


def get_new_entity_instance_photo(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        photo = 'photo'
    else:
        pass
    new_instance_contact_info_message = bot.send_message(message.chat.id, 'Please, send a new ' + photo + ':',
                                                         reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(new_instance_contact_info_message, add_new_entity_instance, photo,
                                   entity_name)


def add_new_entity_instance(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    # temp_data_dict[previous_attribute] = message.text
    temp_data_dict[previous_attribute] = None
    if entity_name == 'Employee':
        response_result = requests.put(service_URL + '/employees/add', json.dumps(temp_data_dict),
                                       headers={'Content-Type': 'application/json'})
        message.text = 'Employees'
    show_data(message)


def perform_actions_with_instance(message: types.Message, entity_name: str):
    if message.text == 'Add a new one':
        bot.send_message(message.chat.id, 'Please, type a new entity identifier:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_new_entity_instance_name, entity_name)
    elif message.text == 'Edit':
        bot.send_message(message.chat.id, 'Please, type an entity identifier:',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, show_entity_instance, 'Employees')
    elif message.text == 'Remove':
        instance_id_message = bot.send_message(message.chat.id, 'Please, type an entity identifier to remove:',
                                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(instance_id_message, remove_entity_instance, 'Employees')
    elif message.text == 'Back to entities':
        message.text = 'Yes'
        show_menu(message)
    elif message.text == 'Log out':
        cmd_start(message)
    else:
        chosen_action_message = bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a '
                                                                  'valid option')
        bot.register_next_step_handler(chosen_action_message, perform_actions_with_instance, entity_name)


def show_entity_instance(message: types.Message, chosen_entities: str):
    instance_id = message.text
    global cur_id
    cur_id = instance_id
    response_result = requests.get(service_URL + '/employees' + '/' + cur_id)
    if response_result.status_code == 200:
        dict_from_server = pretty_string([response_result.json()])
        bot.send_message(message.chat.id, dict_from_server, parse_mode='Markdown')
        if chosen_entities == 'Employees':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            buttons = ['id', 'name', 'surname', 'position', 'phone number', 'photo']
            keyboard.add(*buttons)
            field_to_edit_message = bot.send_message(message.chat.id, 'Please, select a field to edit:',
                                                     reply_markup=keyboard)
        else:
            pass
    else:
        pass
    bot.register_next_step_handler(field_to_edit_message, get_editing_field_value, chosen_entities)


def get_editing_field_value(message: types.Message, chosen_entities):
    field = message.text
    value_message = bot.send_message(message.chat.id, 'Type a new value for a ' + field + ':')
    bot.register_next_step_handler(value_message, edit_entity_instance, field, chosen_entities)


def edit_entity_instance(message: types.Message, field, chosen_entities: str):
    value = message.text
    to_change_info_dict = {'field': field, 'value': value}
    response_result = requests.put(service_URL + '/employees/edit' + '/' + cur_id,
                                   json.dumps(to_change_info_dict),
                                   headers={'Content-Type': 'application/json'})
    if response_result.status_code == 200:
        message.text = chosen_entities
        show_data(message)
        return
    else:
        pass


def remove_entity_instance(message: types.Message, chosen_entities: str):
    instance_id = message.text
    global cur_id
    cur_id = instance_id
    # response_result = requests.get(service_URL + '/employees' + '/' + cur_id)
    response_result = requests.delete(service_URL + '/employees/delete' + '/' + cur_id)
    if response_result.status_code == 204:
        message.text = chosen_entities
        show_data(message)
        return
    else:
        pass


bot.polling(none_stop=True)

if __name__ == '__main__':
    ...
