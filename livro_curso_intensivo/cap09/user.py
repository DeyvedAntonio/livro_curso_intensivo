class User():
    """Classe criada para responder o exercício 9.3."""

    def __init__(self, first_name, last_name, email, username):
        """Inicializa os atributos da classe."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username


    def describe_user(self):
        """Descrição do usuário."""
        print(f'First name: {self.first_name.title()}, Last name: {self.last_name.title()}, Email: {self.email}')
        print(f'and Username: {self.username.title()}.')


    def greet_user(self):
        """Mensagem de saudação ao usuário."""
        print(f'Seja bem vindo, {self.username} que bom ver você aqui.')


user_0 = User('paulo', 'augusto', 'paulo@paulo', 'paulinho')
user_1 = User('roberto', 'lima', 'roberto@paulo', 'tete')
user_2 = User('sergio', 'silva', 'sergio@paulo', 'serginho')
user_3 = User('rodolfo', 'oliveira', 'rodolfo@paulo', 'rodo')
user_4 = User('carlos', 'nascimento', 'carlos@paulo', 'kaka')

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()