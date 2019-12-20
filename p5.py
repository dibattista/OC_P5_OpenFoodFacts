"""This module launch the projet_5"""
### ce fichier est le dossier principal qui lance le projet P5 avec la commande: python p5.py
### it's the iteraction with the user
### je n'ai pas fait d'environement virtuel du coup il faut mettre en pyhton3 avec la commande:
### alias python=python3

from ConnectDB import ConnectDB


def main():
    db = ConnectDB()

    first_question = input("1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués. ")

    if first_question == "1":
        categorie = input(db.get_categories())
        aliment_choose = input(db.get_aliment(categorie))
        print('you choose: ', aliment_choose)
        nutri_grade = db.get_nutrition_grade(aliment_choose)
        print('nutri_grade in p5', nutri_grade)
        substitu = db.get_substitute_aliment(categorie, nutri_grade)
        print('in p5 substitu', substitu)
        db.backup_substitute(substitu)


    elif first_question == "2":
        print("Voici la liste de vos alliment sauvegarder")
    else: input("1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués. ")

if __name__ == "__main__":
    main()
