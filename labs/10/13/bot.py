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

bot = telebot.TeleBot('')

users_engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/users')
Session = sessionmaker(bind=users_engine)
cur_users_session = Session()


@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['Log in', 'Sign in', 'Exit']
    keyboard.add(*buttons)
    inner_message = bot.send_message(message.chat.id, 'Please, select an option', reply_markup=keyboard)
    bot.register_next_step_handler(inner_message, provide_entry_actions)


def provide_entry_actions(message: types.Message):
    if message.text == 'Log in':
        user_login_message = bot.send_message(message.chat.id, 'Enter your login',
                                              reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(user_login_message, check_login)
    elif message.text == 'Sign in':
        user_login_message = bot.send_message(message.chat.id, 'Enter your login',
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
    user_password_message = bot.send_message(message.chat.id, 'Enter your password')
    bot.register_next_step_handler(user_password_message, add_new_user, login)


def add_new_user(message: types.Message, login: str):
    DBUtils.add_entity_instance(cur_users_session, User(login=login, password=message.text, role='user'))
    cur_users_session.commit()


def check_login(message: types.Message):
    users_query = DBUtils.get_entity_data(cur_users_session, User)
    for instance in users_query:
        if instance.login == message.text:
            user_password_message = bot.send_message(message.chat.id, 'Enter your password')
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
            bot.register_next_step_handler(message, show_menu, instance)
            return
    user_password_message = bot.send_message(message.chat.id, 'Error: incorrect password. Enter your password again')
    bot.register_next_step_handler(user_password_message, check_password)


def show_menu(message: types.Message, user: User):
    if message.text == 'Yes':
        if user.role == 'admin':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            buttons = ['Employees']
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Choose an entity to manage', reply_markup=keyboard)
            bot.register_next_step_handler(message, show_data, user)
    elif message.text == 'No':
        cmd_start(message)
    else:
        bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a valid option')
        bot.register_next_step_handler(message, show_menu, user)


def show_data(message, user: User):
    if message.text == 'Employees':
        response_result = requests.get(service_URL + '/employees')
        dict_from_server = pretty_string(response_result.json())
        keyboard = types.InlineKeyboardMarkup()
        pressed_button = keyboard.add(types.InlineKeyboardButton(text="+", callback_data="get_new_entity_instance_id:Employee"))
        bot.send_message(message.chat.id, dict_from_server, reply_markup=keyboard, parse_mode='Markdown')
        employee_id_message = bot.send_message(message.chat.id, 'Select an employee id for further actions or '
                                                                'simply add a new one',
                                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(employee_id_message, show_actions_with_entity_instance, user, pressed_button)
    else:
        bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a valid option')
        bot.register_next_step_handler(message, show_data, user)


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


@bot.callback_query_handler(func=lambda call: call.data.startswith('get_new_entity_instance_id'))
def add_a_new_entity_instance(call):
    global temp_data_dict
    temp_data_dict = {}
    entity_name = call.data.split(':')[1]
    if entity_name == 'Employee':
        identifier = 'id'
    else:
        pass
    new_instance_id_message = bot.send_message(call.message.chat.id, 'Please, type a new ' + identifier + ':')
    bot.register_next_step_handler(new_instance_id_message, get_new_entity_instance_name, identifier, entity_name)


def get_new_entity_instance_name(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        name = 'name'
    else:
        pass
    new_instance_name_message = bot.send_message(message.chat.id, 'Please, type a new ' + name + ':')
    bot.register_next_step_handler(new_instance_name_message, get_new_entity_instance_surname, name, entity_name)


def get_new_entity_instance_surname(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        surname = 'surname'
    else:
        pass
    new_instance_surname_message = bot.send_message(message.chat.id, 'Please, type a new ' + surname + ':')
    bot.register_next_step_handler(new_instance_surname_message, get_new_entity_instance_position, surname, entity_name)


def get_new_entity_instance_position(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        position = 'position'
    else:
        pass
    new_instance_position_message = bot.send_message(message.chat.id, 'Please, type a new ' + position + ':')
    bot.register_next_step_handler(new_instance_position_message, get_new_entity_instance_contact_info, position, entity_name)


def get_new_entity_instance_contact_info(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        contact_info = 'contact_info'
    else:
        pass
    new_instance_contact_info_message = bot.send_message(message.chat.id, 'Please, type a new :' + contact_info + ':')
    bot.register_next_step_handler(new_instance_contact_info_message, get_new_entity_instance_photo, contact_info, entity_name)


def get_new_entity_instance_photo(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    temp_data_dict[previous_attribute] = message.text
    if entity_name == 'Employee':
        photo = 'photo'
    else:
        pass
    new_instance_photo_message = bot.send_message(message.chat.id, 'Please, send a new :' + photo + ':')
    bot.register_next_step_handler(new_instance_photo_message, add_new_entity_instance, photo, entity_name)


def add_new_entity_instance(message: types.Message, previous_attribute, entity_name):
    global temp_data_dict
    # temp_data_dict[previous_attribute] = message.text
    temp_data_dict[previous_attribute] = 'None'
    if entity_name == 'Employee':
        response_result = requests.put(service_URL + '/employees/add', json.dumps(temp_data_dict), headers={'Content-Type': 'application/json'})


def show_actions_with_entity_instance(message: types.Message, user: User, pressed_button):
    if pressed_button.keyboard[0][0].text == '+':
        return
    instance_id = message.text
    global cur_id
    cur_id = instance_id
    response_result = requests.get(service_URL + '/employees' + '/' + instance_id)
    if response_result.status_code == 200:
        dict_from_server = pretty_string([response_result.json()])
        bot.send_message(message.chat.id, dict_from_server, parse_mode='Markdown')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        buttons = ['Edit', 'Remove', 'Back to entities', 'Exit']
        keyboard.add(*buttons)
        chosen_action_message = bot.send_message(message.chat.id, 'Please, select an option', reply_markup=keyboard)
        bot.register_next_step_handler(chosen_action_message, perform_actions_with_instance, user)
    else:
        instance_id_message = bot.send_message(message.chat.id, 'Error: incorrect identifier was provided. Try again',
                                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(instance_id_message, show_actions_with_entity_instance, user)


def perform_actions_with_instance(message: types.Message, user: User):
    if message.text == 'Edit':
        pass
    elif message.text == 'Remove':
        response_result = requests.delete(service_URL + '/employees/delete' + '/' + cur_id)
        if response_result.status_code != 204:
            pass
    elif message.text == 'Back to entities':
        message.text = 'Yes'
        show_menu(message, user)
    elif message.text == 'Exit':
        cmd_start(message)
    else:
        chosen_action_message = bot.send_message(message.chat.id, 'Please, stop typing nonsense and choose a '
                                                                  'valid option')
        bot.register_next_step_handler(chosen_action_message, perform_actions_with_instance, user)


bot.polling(none_stop=True)

if __name__ == '__main__':
    ...
