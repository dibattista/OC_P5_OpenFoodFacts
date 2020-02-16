import requests

class ApiManager:
    """Class ApiManager get the datas from the API Open Food Facts."""

    def __init__(self):
        print('hello api')
        self.URL = "https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&countries=France&tag_contains_0=contains&search_simple=1&action=process&page_size=1&page=1&json=1"
        self.categories = ['Chocolate', 'Fish', 'Fruit', 'Pasta', 'Milk']

    def json_data(self, category):
        payload = {'tag_0': category }
        response = requests.get(self.URL, params=payload)

        json_products = response.json()
        products_values = json_products.get('products')
        return products_values
