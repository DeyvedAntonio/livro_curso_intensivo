class Restaurant():
    """Classe criada para responder o exercício 9.1"""
    
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Método responsável pela inicialização dos atribuitos.
        restaurant_name: nome do restaurante;
        cuisine_type: tipo de cozinha."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    

    def describe_restaurant(self):
        """descrever o restaurante, informa nome e tipo de comida."""
        print(f'Restaurant name is {self.restaurant_name.title()}')
        print(f'Cuisine type is {self.cuisine_type.title()}')


    def open_restaurant(self):
        """Informa que o restaurante está aberto."""
        print('Restaurant is open!')


    def set_number_served(self, number):
        """Permite definir o número de clientes atendidos."""
        self.number_served = number


    def increment_number_served(self, total):
        """Permite incrementar o número de clientes atendidos."""
        self.number_served += total


restaurant = Restaurant('Bonna', 'fast food')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_favorite = Restaurant('DIMI', 'fast food')
restaurant_0 = Restaurant('habbi', 'fast food')
restaurant_1 = Restaurant('rei do bolo', 'caseira')

restaurant_0.describe_restaurant()
restaurant_favorite.describe_restaurant()
restaurant_1.describe_restaurant()

restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(6)
print(restaurant.number_served)
