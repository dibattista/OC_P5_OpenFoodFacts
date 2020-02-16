# coding=utf-8

import random
import os
import mysql.connector

from mysql.connector import Error


class ConnectDB:
    """Class ConnectDB create the database and insert datas in it."""

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.environ.get("YOUR_HOST", ''),
            database=os.environ.get("NAME_DATABASE", ''),
            user=os.environ.get("USER_NAME", ''),
            password=os.environ.get("PASSWORD_DATABASE", '')
        )

    def insert_category(self, category):
        """
                    ### TO DO WRITE GOOD COMMENTE: ici on ajoute les category dans la table categories
        """
        cursor = self.mydb.cursor()
        cursor.execute('INSERT INTO categories (name) VALUES (%s);', (category ,))
        self.mydb.commit()
        print(cursor.rowcount, "record inserted in categories.")

    def insert_aliments(self, val_aliment, categories_id):
        """
                    ### TO DO WRITE GOOD COMMENTE
                    ici on ajoute les aliemnts trouver dans l'api openfoodfacts dans la table aliment
        """
        cursor = self.mydb.cursor()

        sql = "INSERT INTO aliment (product_name, stores, url, nutrition_grades, categories_id) VALUES ( %s, %s, %s, %s, %s );"
        val = (val_aliment['product_name'], val_aliment['stores'], val_aliment['url'], val_aliment['nutrition_grades'], categories_id)
        cursor.execute(sql, val)
        self.mydb.commit()

        print(cursor.rowcount, "record inserted in aliment.")


    def drop_db(self):
        # ici on suprime la db
        cursor = self.mydb.cursor()

        sql = 'DROP DATABASE project_5'
        self.mydb.commit()
        cursor.execute(sql)
        print("DROP DATABASE project_5")

    def create_db(self):
        # ici on creer la db
        new_mydb = mysql.connector.connect(
            host=os.environ.get("YOUR_HOST", ''),
            user=os.environ.get("USER_NAME", ''),
            password=os.environ.get("PASSWORD_DATABASE", '')
        )

        mycursor = new_mydb.cursor()

        mycursor.execute("CREATE DATABASE project_5; USE `project_5` ")

        print("CREATE DATABASE project_5")

    def create_table_categories(self):
        # ici on creer la table categories
        cursor = self.mydb.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS `project_5`.`categories`' \
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

        sql = 'CREATE TABLE IF NOT EXISTS `project_5`.`aliment` (' \
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
            'REFERENCES `project_5`.`categories` (`id`) ' \
            'ON DELETE NO ACTION ' \
            'ON UPDATE NO ACTION) ' \
            'ENGINE = InnoDB;'

        self.mydb.commit()
        cursor.execute(sql)
        print("CREATE table aliment")

    def create_table_substitute_aliment(self):
        # ici on creer la table substitute_aliment
        cursor = self.mydb.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS `project_5`.`substitute_aliment` (' \
                '`id_substitute_aliment` INT NOT NULL auto_increment, ' \
                '`aliment_id` INT NOT NULL, ' \
                'PRIMARY KEY (`id_substitute_aliment`), ' \
                'INDEX `fk_substitute_aliment_aliment_idx` (`aliment_id` ASC) VISIBLE, ' \
                'CONSTRAINT `fk_substitute_aliment_aliment` ' \
                'FOREIGN KEY (`aliment_id`) ' \
                'REFERENCES `project_5`.`aliment` (`id`) ' \
                'ON DELETE NO ACTION ' \
                'ON UPDATE NO ACTION) ' \
                'ENGINE = InnoDB;'


        self.mydb.commit()
        cursor.execute(sql)
        print("CREATE table substitute_aliment")
