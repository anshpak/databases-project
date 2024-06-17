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


@app.route("/employees/delete/<int:id>", methods=['DELETE'])
def delete_subject_bu_id(id_):
    DBUtils.remove_entity_instance(cur_session, employees_query, Employee, id_)
    cur_session.commit()
    return make_response("", 204)


@app.route("/student/add/<int:id>", methods=['PUT'])
def edit_student_by_id(id):
    input_data = request.get_json()
    cur_stud = dal.get_stud_by_id(id) # type: Student
    for key in input_data:
        if key != "id":
            setattr(cur_stud, key, input_data[key])
        else:
            pass
    dal.commit()
    return jsonify(cur_stud.serialize())



if __name__ == '__main__':
    pass
