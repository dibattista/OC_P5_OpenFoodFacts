#####  TO DO  faire une nouvelle classe : interaction user
import random
import os

import mysql.connector

from mysql.connector import Error


class SelectApi:
    def __init__(self):
        """
            ### TO DO WRITE GOOD COMMENTE:
            connection a la db
        """

        self.mydb = mysql.connector.connect(
            host=os.environ.get("YOUR_HOST", ''),
            database=os.environ.get("NAME_DATABASE", ''),
            user=os.environ.get("USER_NAME", ''),
            password=os.environ.get("PASSWORD_DATABASE", '')
        )
        # if self.mydb.is_connected():
        #     print('Connected to MySQL database projet_5')

    def get_categories(self):
        cursor = self.mydb.cursor()
        result = []
        cursor.execute("SELECT * FROM categories;")
        #print('X          Choose a number from a categories list:       X')
        myresult = cursor.fetchall()
        for x in myresult:
            result.append(x)
            #print(x)
        return result

    def get_aliment(self, categories_id):
        cursor = self.mydb.cursor()

        cursor.execute(
            "SELECT id, product_name, nutrition_grades FROM aliment WHERE categories_id = " + categories_id)
        myresult = cursor.fetchall()
        return myresult

    def get_nutrition_grade(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT nutrition_grades FROM aliment where id =" + id)
        myresult = cursor.fetchall()
        for result in myresult:
            ## print('result in ConnectDB', result[0])
            return result[0]

    def get_substitute_aliment(self, categories_id, nutri_grade_choose):
        cursor = self.mydb.cursor()

        if nutri_grade_choose == 'a':
                cursor.execute(
                    "SELECT * FROM aliment WHERE categories_id =" + categories_id + " AND nutrition_grades = 'a'")
                myresult = cursor.fetchall()
                #print('myresult in get_substitute_aliment SELECTAPIDATA in IF: ', myresult)
                # because i don't know how to choose the result of the multiple substitue a have, i propose random
                #return random.choice(myresult)
                return myresult
        # trouver des aliments avec un nutrition grades inferieur a celui de la presente recherche (nutri_grade_choose) dans la categories choisi
        else:
            cursor.execute(
                "SELECT * FROM aliment WHERE categories_id =" + categories_id + " AND nutrition_grades < '%s'" % nutri_grade_choose)
    
            myresult = cursor.fetchall()
            #print('myresult in get_substitute_aliment SELECTAPIDATA in ELSE: ', myresult)
            # because i don't know how to choose the result of the multiple substitue a have, i propose random
            #return random.choice(myresult)
            return myresult

    def backup_substitute(self, substitute):
        cursor = self.mydb.cursor()
        cursor.execute(
            "INSERT INTO substitut_aliment (aliment_id) VALUES (%s);", (substitute[0],))

        self.mydb.commit()

        print(cursor.rowcount, "save new substitute")

    ## substitue d'aliment sauvegarder

    def get_aliment_substitute(self, aliment_id):
        id = aliment_id
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM aliment where id = '%d'" % id)
        myresult = cursor.fetchall()
        return myresult

    def get_all_substitute(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT aliment_id FROM substitut_aliment;")
        myresult = cursor.fetchall()
        return myresult
