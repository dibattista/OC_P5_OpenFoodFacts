# coding=utf-8

from DataBase.connectDB import ConnectDB

class NewDB:
    """Class NewDB call the fonction to create the database with the tables"""

    def __init__(self):
        self.db = ConnectDB()

    def create_db(self):
        self.db.drop_db()
        self.db.create_db()
        self.db.create_table_categories()
        self.db.create_table_aliment()
        self.db.create_table_substitute_aliment()
