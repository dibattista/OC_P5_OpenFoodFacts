# coding=utf-8

"""This is the class to connect at the data base"""

import random
import os
import mysql.connector

from mysql.connector import Error


class ConnectDB:

    def __init__(self):
        """
            ### TO DO WRITE GOOD COMMENTE:
            connection a la db
        """
        try:
            self.mydb = mysql.connector.connect(
                host=os.environ.get("YOUR_HOST", ''),
                database=os.environ.get("NAME_DATABASE", ''),
                user=os.environ.get("USER_NAME", ''),
                password=os.environ.get("PASSWORD_DATABASE", '')
            )
            if self.mydb.is_connected():
                print('Connected to MySQL database projet_5')


        except Error as e:
            print(e)



    def insert_category(self, category):
        """
                    ### TO DO WRITE GOOD COMMENTE: ici on ajoute les category dans la table categories
        """
        cursor = self.mydb.cursor()

        # cette syntaxe marche pour un insert avec une valeur (category)
        # la virgule fait en sort que ça marche (category ,))
        # on a pas besoin de la mettre avec deux valeurs exemple (category, id)
        cursor.execute('INSERT INTO categories (name) VALUES (%s);', (category ,))
        self.mydb.commit()
        print(cursor.rowcount, "record inserted in categories.")

    def insert_aliments(self, val_aliment, categories_id):
        """
                    ### TO DO WRITE GOOD COMMENTE
                    ici on ajoute les aliemnts trouver dans l'api openfoodfacts dans la table aliment
        """
        # the cursor permet l'insert en base
        cursor = self.mydb.cursor()

        # si dessous on prepare la requet pour inserer en db les aliments de l'api trouver avec le get
        sql = "INSERT INTO aliment (product_name, stores, url, nutrition_grades, categories_id) VALUES ( %s, %s, %s, %s, %s );"
        # si dessous on recupere les valeurs pour chaque key scpecifique, trouver dans le get des aliments de api openfoodfacts
        val = (val_aliment['product_name'], val_aliment['stores'], val_aliment['url'], val_aliment['nutrition_grades'], categories_id)
        # si dessous on excute l insert en db
        cursor.execute(sql, val)
        # si dessous le commit valide la requet sinon rien de se passe pas d'insertion en db
        self.mydb.commit()

        print(cursor.rowcount, "record inserted in aliment.")


    def drop_db(self):
        # ici on suprime la db
        cursor = self.mydb.cursor()

        sql = 'DROP DATABASE projet_5'
        self.mydb.commit()
        cursor.execute(sql)
        print("DROP DATABASE projet_5")

    def create_db(self):
        # ici on creer la db
        new_mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="8783Bb@10071957"
        )

        mycursor = new_mydb.cursor()

        mycursor.execute("CREATE DATABASE projet_5; USE `projet_5` ")

        print("CREATE DATABASE projet_5")

    def create_table_categories(self):
        # ici on creer la table categories
        cursor = self.mydb.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS `projet_5`.`categories`' \
            '(`id` INT NOT NULL auto_increment, ' \
            '`name` VARCHAR(30) NOT NULL,' \
            'PRIMARY KEY (`id`))' \
            'ENGINE = InnoDB;'

        self.mydb.commit()
        cursor.execute(sql)
        print("CREATE table categories")

    def create_table_aliment(self):
        # ici on creer la table aliment
        cursor = self.mydb.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS `projet_5`.`aliment` (' \
            '`id` INT NOT NULL auto_increment, ' \
            '`product_name` VARCHAR(1000) NOT NULL, ' \
            '`stores` VARCHAR(1000) NOT NULL, ' \
            '`url` VARCHAR(1000) NOT NULL, ' \
            '`nutrition_grades` VARCHAR(1000) NOT NULL, ' \
            '`categories_id` INT NOT NULL, ' \
            'PRIMARY KEY (`id`), ' \
            'INDEX `fk_aliment_categories1_idx` (`categories_id` ASC) VISIBLE, ' \
            'CONSTRAINT `fk_aliment_categories1` ' \
            'FOREIGN KEY (`categories_id`) ' \
            'REFERENCES `projet_5`.`categories` (`id`) ' \
            'ON DELETE NO ACTION ' \
            'ON UPDATE NO ACTION) ' \
            'ENGINE = InnoDB;'

        self.mydb.commit()
        cursor.execute(sql)
        print("CREATE table aliment")

    def create_table_substitut_aliment(self):
        # ici on creer la table substitut_aliment
        cursor = self.mydb.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS `projet_5`.`substitut_aliment` (' \
                '`idsubstitut_aliment` INT NOT NULL auto_increment, ' \
                '`aliment_id` INT NOT NULL, ' \
                'PRIMARY KEY (`idsubstitut_aliment`), ' \
                'INDEX `fk_substitut_aliment_aliment_idx` (`aliment_id` ASC) VISIBLE, ' \
                'CONSTRAINT `fk_substitut_aliment_aliment` ' \
                'FOREIGN KEY (`aliment_id`) ' \
                'REFERENCES `projet_5`.`aliment` (`id`) ' \
                'ON DELETE NO ACTION ' \
                'ON UPDATE NO ACTION) ' \
                'ENGINE = InnoDB;'


        self.mydb.commit()
        cursor.execute(sql)
        print("CREATE table substitut_aliment")

#####  TO DO  faire une nouvelle classe : interaction user

#     def get_categories(self):
#         cursor = self.mydb.cursor()
#
#         cursor.execute("SELECT * FROM categories;")
#         print('X          Choose a number from a categories list:       X')
#         myresult = cursor.fetchall()
#         for x in myresult:
#             print(x)
#
#
#     def get_aliment(self, categories_id):
#         cursor = self.mydb.cursor()
#
#         cursor.execute("SELECT id, product_name, nutrition_grades FROM aliment WHERE categories_id = " + categories_id)
#         myresult = cursor.fetchall()
#         print('X           Choose a number from a aliment list:         X')
#         for x in myresult:
#             print(x)
#
#
#     def get_nutrition_grade(self, id):
#         cursor = self.mydb.cursor()
#         cursor.execute("SELECT nutrition_grades FROM aliment where id =" + id)
#         myresult = cursor.fetchall()
#         for result in myresult:
#             ## print('result in ConnectDB', result[0])
#             return result[0]
#
#
#     def get_substitute_aliment(self, categories_id, nutri_grade_choose):
#         cursor = self.mydb.cursor()
#         symbol = nutri_grade_choose
#
#         # trouver des aliments avec un nutrition grades inferieur a celui de la presente recherche (nutri_grade_choose) dans la categories choisi
#         cursor.execute(
#             "SELECT id, product_name, stores, url FROM aliment WHERE categories_id =" + categories_id + " AND nutrition_grades < '%s'" % symbol)
#
#         myresult = cursor.fetchall()
#         # because i don't know how to choose the result of the multiple substitue a have, i propose random
#         return random.choice(myresult)
#
#
#     def backup_substitute(self, substitute):
#         cursor = self.mydb.cursor()
#         cursor.execute("INSERT INTO substitut_aliment (aliment_id) VALUES (%s);", (substitute[0],))
#
#         self.mydb.commit()
#
#         print(cursor.rowcount, "save new substitute")
#
#
# ## substitue d'aliment sauvegarder
#     def get_aliment_substitute(self, aliment_id):
#         id = aliment_id
#         cursor = self.mydb.cursor()
#         cursor.execute("SELECT * FROM aliment where id = '%d'" % id)
#         myresult = cursor.fetchall()
#         print('myresult', myresult)
#
#
#     def get_all_substitute(self):
#          cursor = self.mydb.cursor()
#          cursor.execute("SELECT aliment_id FROM substitut_aliment;")
#          myresult = cursor.fetchall()
#          return myresult
#
#
#
#
#


