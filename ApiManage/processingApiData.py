# coding=utf-8

from ApiManage.apiManager import ApiManager
from DataBase.connectDB import ConnectDB


def export_data_json(products_values):
    liste_product = []

    for product in products_values:
        result = {'product_name': '', 'stores': '', 'url': '', 'nutrition_grades': ''}
        try:
            for k in result:
                result[k] = product[k]

            liste_product.append({k: v for k, v in result.items() if v is not None})
        except:
            pass
    return liste_product


class Data():
    """Class Data clean the json from API and insert this datas in database."""

    def __init__(self):
        self.api_data = ApiManager()
        # DB connection
        self.db = ConnectDB()

    def add_categories(self):
        for i in range(len(self.api_data.categories)):
            self.db.insert_category(self.api_data.categories[i])


    def insert_aliments(self):
        for i in range(len(self.api_data.categories)):
            products_values = self.api_data.json_data(self.api_data.categories[i])
            products_values_clean = export_data_json(products_values)

            for product_clean in products_values_clean:
                if product_clean["stores"]:
                    self.db.insert_aliments(product_clean, i + 1)
                




