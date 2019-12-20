from ConnectDB import ConnectDB


### TO USE THE CLASS, I CREATE A OBJECT, exemple db = ConnectDB()
### IF NOT A NEW CLASS WILL BE CREATE ALL THE TIME WITH : Request().fonction()

class NewDB:
    def __init__(self):
        self.db = ConnectDB()

    def create_db(self):
        self.db.drop_db()
        self.db.create_db()
        self.db.create_table_categories()
        self.db.create_table_aliment()
        self.db.create_table_substitut_aliment()
