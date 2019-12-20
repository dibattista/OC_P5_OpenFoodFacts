"""This module launch the projet_5"""
### ce fichier est le dossier principal qui lance le projet P5 avec la commande: python p5.py
### verification de la base avex MySQLWorkBench
### je n'ai pas fait d'environement virtuel du coup il faut mettre en pyhton3 avec la commande:
### alias python=python3
import pprint;

from Request import Request
from ConnectDB import ConnectDB
pp = pprint.PrettyPrinter(indent=4)


"""
        ### TO DO WRITE GOOD COMMANTE:
        The method clean the data to have a list of dictonary with key and value need for the insert
        exemple: {'product_name': 'Nesquik', 'stores': '', 'url': 'https://world.openfoodfacts.org/product/7613035239562/nesquik-nestle', 'nutrition_grades': 'd'}
"""
def export_data_json(products_values):
    liste_product = []
    for product in products_values:
        result = {'product_name': '', 'stores': '', 'url': '', 'nutrition_grades': ''}
        try:
            for k in result:
                ### ici on récupère la valeur pour chaque key comme product[product_name] = Nesquik
                result[k] = product[k]
            ### ici on construit une list ou on aurra k la key et leurs valeurs dans un dictonary avec les quatres key
            ### comme dans result
            liste_product.append({k: v for k, v in result.items() if v is not None})
        except:
            pass

    return liste_product

def main():
    ### TO USE THE CLASS, I CREATE A OBJECT, exemple db = ConnectDB()
    ### IF NOT A NEW CLASS WILL BE CREATE ALL THE TIME WITH : Request().fonction()

    # get data from API openfoodfacts
    request = Request()
    # CONNECTION TO DB
    db = ConnectDB()

    ###### TO DO
    # mettre dans un fichier à part car ce n'est que pour le travail pas besoin dans le projet
    ######
    #db.drop_db()
    #db.create_db()
    #db.create_table_categories()
    #db.create_table_aliment()
    #db.create_table_substitut_aliment()
    ####### END TO DO

    """
            ### TO DO WRITE GOOD COMMANTE:
            The first loop itere the categories to get the product from the API openfoodfacts for each category
            Then we clean the result to have a list ready to insert in db.
            The second loop iter the list to have access each dictonary
    """
    #for i in range(len(request.categories)):
        #### ici on recupère les produits des categories choisie grace à la requet get de API openfoodfacts
        #products_values = request.json_data(request.categories[i])
        #### ici on nettoye le resulta de la request get obtenu si dessus
        #products_values_clean = export_data_json(products_values)

        ### si dessous ligne pour inset les categories à décommanter en cas de besoin
        ### je m'en sert quand j'ai supprimer et rajouter la db, alors la table categories se trouve vide
        ### et je la remplit avec cette insert pour pouvoir faire l'insert aliment
        #db.insert_category(request.categories[i])

        #for product_clean in products_values_clean:
            #print('product_clean', product_clean)
            #### bien garder le i + 1 car index commance à 0 et du coup si on ne met pas + 1 cela ne marche pas
            ## si dessous on fait insert des aliment en fonction des categories choisi et leur index (i) qui et lie
            ## la table aliment par une FOREIGN KEY a la table categories
            #db.insert_aliments(product_clean, i + 1)

    first_question = input("1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués. ")

    if first_question == "1":
        ## 'trouver un moyen de recupérer les categiries en dynamique avec les chiffres'
        ## print('Sélectionnez le chiffre de la catégorie')

        categorie = input(db.get_categories())
        aliment_choose = input(db.get_aliment(categorie))
        print('you choose: ', aliment_choose)
        nutri_grade = db.get_nutrition_grade(aliment_choose)
        print('nutri_grade in p5', nutri_grade)
        substitu = db.get_substitute_aliment(categorie, nutri_grade)
        print('in p5 substitu', substitu)
        db.backup_substitute(substitu)




    elif test_number == "2":
        print("Voici la liste de vos alliment sauvegarder")
    else: input("1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués. ")

if __name__ == "__main__":
    ####???? est-ce que l'interaction client peur se faire comme ça ?
    # question_user = input('Quel aliment souhaitez-vous remplacer ? ')
    # find_aliment = input('Retrouver mes aliments substitués.')
    #  if find_aliment == 1 :
    #      question suivant
    main()
