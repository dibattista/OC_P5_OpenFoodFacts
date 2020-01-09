# coding=utf-8

from ApiManage.apiManager import ApiManager
from DataBase.connectDB import ConnectDB

# """
#         ### TO DO WRITE GOOD COMMANTE:
#         The method clean the data to have a list of dictonary with key and value need for the insert
#         exemple: {'product_name': 'Nesquik', 'stores': '', 'url': 'https://world.openfoodfacts.org/product/7613035239562/nesquik-nestle', 'nutrition_grades': 'd'}
# """

def export_data_json(products_values):
    liste_product = []
    for product in products_values:
        result = {'product_name': '', 'stores': '', 'url': '', 'nutrition_grades': ''}
        try:
            for k in result:
                ### ici on recupère la valeur pour chaque key comme product[product_name] = Nesquik
                result[k] = product[k]
            ### ici on construit une list ou on aurra k la key et leurs valeurs dans un dictonary avec les quatres key
            ### comme dans result
            liste_product.append({k: v for k, v in result.items() if v is not None})
        except:
            pass

    return liste_product


class Data():
    def __init__(self):
        ## changer name of self.api_data
        self.api_data = ApiManager()
        # CONNECTION TO DB
        self.db = ConnectDB()

    def add_categories(self):
        for i in range(len(self.api_data.categories)):
            self.db.insert_category(self.api_data.categories[i])


    def insert_aliments(self):
        for i in range(len(self.api_data.categories)):
            # ici on recupère les produits des categories choisie grace à la requet get de API openfoodfacts
            products_values = self.api_data.json_data(self.api_data.categories[i])
            #### ici on nettoye le resulta de la api_data get obtenu si dessus
            products_values_clean = export_data_json(products_values)

            for product_clean in products_values_clean:
                # bien garder le i + 1 car index commance à 0 et du coup si on ne met pas + 1 cela ne marche pas
                ## si dessous on fait insert des aliment en fonction des categories choisi et leur index (i) qui et lie
                ## la table aliment par une FOREIGN KEY a la table categories
                self.db.insert_aliments(product_clean, i + 1)





