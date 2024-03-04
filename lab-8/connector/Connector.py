import mysql.connector

from patterns.SingletonMeta import SingletonMeta


class Connector(metaclass=SingletonMeta):
    def __init__(self, host, user, password, database, singleton_check):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.singleton_check = singleton_check

    def connect(self, successful_report=False):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if successful_report:
                print("Connection successful!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
        SingletonMeta.delete_instance(Connector)
