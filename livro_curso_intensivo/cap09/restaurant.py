class Restaurant():
    """Classe criada para responder o exercício 9.1"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name.title()}')
        print(f'Cuisine type is {self.cuisine_type.title()}')


    def open_restaurant(self):
        print('Restaurant is open!')


restaurant = Restaurant('Bonna', 'fast food')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
