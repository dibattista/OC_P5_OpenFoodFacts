# coding=utf-8

"""This module launch the projet_5"""
### ce fichier est le dossier principal qui lance le projet P5 avec la commande: python main.py
## or python main.py -n pour creer un nouvelle base
### alias python=python3

import argparse
import os


from BetterFood.betterFood import BetterFood
from DataBase.createDB import NewDB
from ApiManage.processingApiData import Data

def main():

    ap = argparse.ArgumentParser()

    ap.add_argument('-n', '--new',
                help="create new data base", action='store_true')
    args = ap.parse_args()


    if args.new:
        new_db = NewDB()
        new_db.create_db()
        ## add datas
        data_api = Data()
        data_api.add_categories()
        data_api.insert_aliments()
    else:
        start = BetterFood()
        start.startFinding()


if __name__ == "__main__":
    main()
