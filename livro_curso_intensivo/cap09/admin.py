from user import User

class Admin(User):
    """Classe criada para resolver o exercício 9.7."""
    def __init__(self, first_name, last_name, email, username, *privileges):
        super().__init__(first_name, last_name, email, username)
        self.privileges = privileges
    

