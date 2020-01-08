"""This is the class to extracting the data from the API Open Food Facts"""
import requests, pprint;
pp = pprint.PrettyPrinter(indent=4)

class ApiManager:
    def __init__(self):
        ## !!!! THE products = requests.get(url=self.URL, params=self.PARAMS) Doesnt' work some time try a while?
        self.URL = "https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&countries=France&tag_contains_0=contains&search_simple=1&action=process&page_size=1&page=1&json=1"
        self.categories = ['Chocolate', 'Fish', 'Fruit', 'Pasta', 'Milk']

    def json_data(self, category):
        payload = {'tag_0': category }
        response = requests.get(self.URL, params=payload)
        #response = requests.get(self.URL)
        #print('ICI URL', response.url)


        json_products = response.json()
        products_values = json_products.get('products')
        return products_values
