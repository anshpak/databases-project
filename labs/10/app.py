from flask import Flask
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_access.db_utils import DBUtils
from models.skydiving import Employee

engine = create_engine('mysql+pymysql://root:sic mundus creatus est@localhost/skydiving')
Session = sessionmaker(bind=engine)
cur_session = Session()
app = Flask(__name__)


@app.route("/")
def main():
    return f"Hello!"


@app.route("/employees", methods=['GET'])
def show_employees():
    data_list = DBUtils.get_entity_data(cur_session, Employee).scalar().all()
    return jsonify([elem.serialize() for elem in data_list])


if __name__ == '__main__':
    input()
