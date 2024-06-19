from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_access.db_utils import DBUtils
from models.skydiving import Employee

engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/skydiving')
Session = sessionmaker(bind=engine)
cur_session = Session()
app = Flask(__name__)
employees_query = DBUtils.get_entity_data(cur_session, Employee)


@app.route("/")
def main():
    return f"Hello!"


@app.route("/employees", methods=['GET'])
def show_employees():
    return jsonify([instance.serialize() for instance in employees_query])


@app.route("/employees/<int:id_>", methods=['GET'])
def show_employee_by_id(id_):
    instance = DBUtils.get_entity_instance(employees_query, Employee, id_)
    return jsonify(instance.serialize())


@app.route("/employees/delete/<int:id_>", methods=['DELETE'])
def remove_employee_by_id(id_):
    DBUtils.remove_entity_instance(cur_session, employees_query, Employee, id_)
    cur_session.commit()
    return make_response("", 204)


@app.route("/employees/add", methods=['PUT'])
def add_entity_instance():
    print('here')
    input_data = request.get_json()
    DBUtils.add_entity_instance(cur_session, Employee(input_data))
    cur_session.commit()
    return make_response("", 204)


@app.route("/employees/edit/<int:id_>", methods=['PUT'])
def edit_employee_by_id(id_):
    input_data = request.get_json()
    instance = DBUtils.get_entity_instance(employees_query, Employee, id_)
    field = input_data['field']
    value = input_data['value']
    setattr(instance, field, value)
    cur_session.commit()
    return jsonify(instance.serialize())


if __name__ == '__main__':
    pass
