# coding=utf-8

import random
import os

import mysql.connector

from mysql.connector import Error


class SelectApi:
    """Class SelectApi select or insert the data from database."""

    def __init__(self):
        """Sets up connection with the MySQL server in argument"""

        self.mydb = mysql.connector.connect(
            host=os.environ.get("YOUR_HOST", ''),
            database=os.environ.get("NAME_DATABASE", ''),
            user=os.environ.get("USER_NAME", ''),
            password=os.environ.get("PASSWORD_DATABASE", '')
        )

    def get_categories(self):
        """Get the all categories from the table categories."""

        cursor = self.mydb.cursor()
        result = []
        cursor.execute("SELECT * FROM categories;")
        myresult = cursor.fetchall()

        # Translate the categories in french
        for x in myresult:
            y = list(x)
            if x[1] == 'Chocolate':
                y[1] = "Chocolat"
                x = tuple(y)

            if x[1] == 'Fish':
                y[1] = "Poisson"
                x = tuple(y)
            
            if x[1] == 'Pasta':
                y[1] = "Pates"
                x = tuple(y)
            
            if x[1] == 'Milk':
                y[1] = "Lait"
                x = tuple(y)

            result.append(x)
        return result

    def get_aliment(self, categories_id):
        """Get the aliments from the table aliment with the id of categories."""

        cursor = self.mydb.cursor()
        cursor.execute(
            "SELECT id, product_name, nutrition_grades FROM aliment WHERE categories_id = " + categories_id)
        myresult = cursor.fetchall()
        return myresult

    def get_nutrition_grade(self, id):
        """Get the nutrition grade from the table aliment with the id of aliment."""

        cursor = self.mydb.cursor()
        cursor.execute("SELECT nutrition_grades FROM aliment where id =" + id)
        myresult = cursor.fetchall()
        for result in myresult:
            return result[0]

    def get_substitute_aliment(self, categories_id, nutri_grade_choose):
        """Get the aliment with the lowest nutrition grade."""

        cursor = self.mydb.cursor()
        # Find the lowest of nutrion_grade of the categories_id
        nutrition_grade_Min = cursor.execute(
            "SELECT Min(nutrition_grades) FROM aliment WHERE categories_id =" + categories_id)
        nutrition_grade_Min = cursor.fetchall()
        
        for min_grade in nutrition_grade_Min:
            # Find a better aliment with the lowest or equal nutrition_grades
            cursor.execute(
                "SELECT * FROM aliment WHERE categories_id =" + categories_id +
                " AND nutrition_grades <= '%s'" % min_grade)
            myresult = cursor.fetchall()
            return myresult


    def backup_substitute(self, substitute):
        """Backup the id of aliment in the table substitute_aliment."""

        cursor = self.mydb.cursor()
        cursor.execute(
            "INSERT INTO substitute_aliment (aliment_id) VALUES (%s);", (substitute,))
        self.mydb.commit()
        print(cursor.rowcount, "save new substitute")

    def get_aliment_substitute(self, aliment_id):
        """Get the aliment with his id."""

        id = aliment_id
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM aliment where id = '%d'" % id)
        myresult = cursor.fetchall()
        return myresult

    def get_all_substitute(self):
        """Get all aliment id in the table substitute_aliment."""

        cursor = self.mydb.cursor()
        cursor.execute("SELECT aliment_id FROM substitute_aliment;")
        myresult = cursor.fetchall()
        return myresult
