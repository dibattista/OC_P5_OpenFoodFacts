# coding=utf-8

"""This module launch this project. Two options are possible:
    1- Creation of database and insertion of datas with 'python main.py -n'
    2- Start the user interface with 'python main.py' """

import argparse
import os


from GUI.gui import Window
from DataBase.createDB import NewDB
from ApiManage.processingApiData import Data

def main():
    """Setup the argument in commande line.
        With the condition 
        start the creation of database or the user interface """

    ap = argparse.ArgumentParser()

    ap.add_argument('-n', '--new',
                help="create new data base", action='store_true')
    args = ap.parse_args()


    if args.new:
        # Create new database
        new_db = NewDB()
        new_db.create_db()

        # Add datas
        data_api = Data()
        data_api.add_categories()
        data_api.insert_aliments()
    else:
        # Start graphical user interface
        window = Window()
        window


if __name__ == "__main__":
    main()
