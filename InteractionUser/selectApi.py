#####  TO DO  faire une nouvelle classe : interaction user
import mysql.connector;

from mysql.connector import Error

class SelectApi:
    def __init__(self):
        """
            ### TO DO WRITE GOOD COMMENTE:
            connection a la db
        """
        try:
            self.mydb = mysql.connector.connect(
                host='localhost',
                database='projet_5',
                user='root',
                password='8783Bb@10071957')
            #if self.mydb.is_connected():
                #print('Connected to MySQL database projet_5')


        except Error as e:
            print(e)

    def get_categories(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM categories;")
        print('X          Choose a number from a categories list:       X')
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)


    def get_aliment(self, categories_id):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT id, product_name, nutrition_grades FROM aliment WHERE categories_id = " + categories_id)
        myresult = cursor.fetchall()
        print('X           Choose a number from a aliment list:         X')
        for x in myresult:
            print(x)


    def get_nutrition_grade(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT nutrition_grades FROM aliment where id =" + id)
        myresult = cursor.fetchall()
        for result in myresult:
            ## print('result in ConnectDB', result[0])
            return result[0]


    def get_substitute_aliment(self, categories_id, nutri_grade_choose):
        cursor = self.mydb.cursor()
        symbol = nutri_grade_choose

        # trouver des aliments avec un nutrition grades inferieur a celui de la presente recherche (nutri_grade_choose) dans la categories choisi
        cursor.execute(
            "SELECT id, product_name, stores, url FROM aliment WHERE categories_id =" + categories_id + " AND nutrition_grades < '%s'" % symbol)

        myresult = cursor.fetchall()
        # because i don't know how to choose the result of the multiple substitue a have, i propose random
        return random.choice(myresult)


    def backup_substitute(self, substitute):
        cursor = self.mydb.cursor()
        cursor.execute("INSERT INTO substitut_aliment (aliment_id) VALUES (%s);", (substitute[0],))

        self.mydb.commit()

        print(cursor.rowcount, "save new substitute")


    ## substitue d'aliment sauvegarder
    def get_aliment_substitute(self, aliment_id):
        id = aliment_id
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM aliment where id = '%d'" % id)
        myresult = cursor.fetchall()
        print('myresult', myresult)


    def get_all_substitute(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT aliment_id FROM substitut_aliment;")
        myresult = cursor.fetchall()
        return myresult
