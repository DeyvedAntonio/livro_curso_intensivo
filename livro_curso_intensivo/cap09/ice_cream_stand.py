from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Classe criada para responder o exercício 9.6."""
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """Método para inicializar os atributos da classe."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    

    def flavors_print(self):
        """Método para imprimir a lista de sabores de sorvete."""
        print(self.flavors)


my_ice_cream = IceCreamStand('Ice Team', 'Sorvetes', 'Uva', 'Morango', 'Chocolate')
my_ice_cream.flavors_print()