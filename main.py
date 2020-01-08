# coding=utf-8

"""This module launch the projet_5"""
### ce fichier est le dossier principal qui lance le projet P5 avec la commande: python main.py
### alias python=python3

import argparse

# from DataBase.connectDB import ConnectDB
from DataBase.createDB import NewDB
from InteractionUser.startInteraction import StartInteraction

ap = argparse.ArgumentParser()
ap.add_argument('-n', '--new',
                help="create new data base", action='store_true')
args = ap.parse_args()


def main():
    print('arg', args.new)
    if args.new:
        # db = ConnectDB()
        new_db = NewDB()
        new_db.create_db()
    else:
        start = StartInteraction()
        start


if __name__ == "__main__":
    main()
