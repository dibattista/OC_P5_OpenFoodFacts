# coding=utf-8

from ApiManage.apiManager import ApiManager
from DataBase.connectDB import ConnectDB


def export_data_json(products_values):
    """Cleaning the json from the API and return the list of dictionary with datas for the table aliment."""

    liste_product = []
    for product in products_values:
        # iteration of the json:

        result = {'product_name': '', 'stores': '', 'url': '', 'nutrition_grades': ''}
        # create a dictionary for insert data in table aliment in database.
        try:
            for k in result:
                # Find the key in dictionary result

                result[k] = product[k]
                # Add values in dictionary result, from json key.

            liste_product.append({k: v for k, v in result.items() if v is not None})
            # Add dictionary in list liste_product without values equal to none.
        except:
            pass
    return liste_product


class Data():
    """Class Data clean the json from API and insert this datas in database."""

    def __init__(self):
        """Param api_data: Get json API.
            Param Database: connection database.
        """
        self.api_data = ApiManager()
        self.db = ConnectDB()

    def add_categories(self):
        """Insert the categories in table categories."""

        for i in range(len(self.api_data.categories)):
            # Iterate the numbers from the length categories list.

            self.db.insert_category(self.api_data.categories[i])
            # Call the fonction to insert the data in table categories in database.


    def insert_aliments(self):
        """Insert the aliments in table aliment."""

        for i in range(len(self.api_data.categories)):
            #Iterate the numbers from the length categories list.

            products_values = self.api_data.json_data(self.api_data.categories[i])
            # Call the fonction to get the json from API for each categories.
            products_values_clean = export_data_json(products_values)
            #  Call the fonction to clean this json.

            for product_clean in products_values_clean:
                # Iterate the dictionary whith the list of data from cleaned json.

                if product_clean["stores"]:
                    # delete the empty string.
                    self.db.insert_aliments(product_clean, i + 1)
                    # Call the fonction to insert the aliments in table aliment in database.

                




