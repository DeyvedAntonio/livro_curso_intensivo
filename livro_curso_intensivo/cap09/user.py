class User():
    """Classe criada para responder o exercício 9.3."""

    def __init__(self, first_name, last_name, email, username):
        """Inicializa os atributos da classe."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = 0


    def describe_user(self):
        """Descrição do usuário."""
        print(f'First name: {self.first_name.title()}, Last name: {self.last_name.title()}, Email: {self.email}')
        print(f'and Username: {self.username.title()}.')


    def greet_user(self):
        """Mensagem de saudação ao usuário."""
        print(f'Seja bem vindo, {self.username} que bom ver você aqui.')


    def increment_login_attempts(self):
        """Incrementa o valor do atributo (login_attempts) em 1."""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reseta o valor do atributo, login_attempts."""
        self.login_attempts = 0


class Privileges():
    """Classe de privilegios dos usuários."""

    def __init__(self, *privileges):
        """Inicialização de atributos da classe Privileges."""
        self.privileges = privileges
    

    def show_privileges(self):
        """Lista o conjunto de privilégios de um administrador."""
        print(self.privileges)


class Admin(User):
    """Classe criada para resolver o exercício 9.7."""
    
    def __init__(self, first_name, last_name, email, username, *privileges):
        """Inicializa os atributos da classe."""
        super().__init__(first_name, last_name, email, username)
        self.privileges = privileges

    # def show_privileges(self):
    #     """Lista o conjunto de privilégios de um administrador."""
    #     print(self.username, self.privileges)
