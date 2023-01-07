class Privileges():
    """Classe de privilegios dos usuários."""

    def __init__(self, *privileges):
        """Inicialização de atributos da classe Privileges."""
        self.privileges = privileges
    

    def show_privileges(self):
        """Lista o conjunto de privilégios de um administrador."""
        print(self.privileges)
    