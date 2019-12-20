"""This is the class to extracting the data from the API Open Food Facts"""
import requests, pprint;
pp = pprint.PrettyPrinter(indent=4)

class Request:
    def __init__(self):
        ## !!!! THE products = requests.get(url=self.URL, params=self.PARAMS) Doesnt' work
        self.URL = "https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&countries=France&tag_contains_0=contains&search_simple=1&action=process&page_size=1&page=1&json=1"
        self.PARAMS = {'tag_0=': "Chocolates"}
        self.categories = ['Chocolates', 'Fishes', 'Fruits', 'Pastas', 'Wines']

    def json_data(self, category):
        payload = {'tag_0': category }
        #print('payload', payload)
        response = requests.get(self.URL, params=payload)
        #response = requests.get(self.URL)
        print('ICI URL', response.url)
        # extracting data in json format
        # products = requests.get(url=self.URL, params=category)
        # print('new URL', requests.get(url=self.URL, params=mydict))
        # print('url', self.URL)

        json_products = response.json()
        #print('json_products', json_products)
        products_values = json_products.get('products')
        return products_values
