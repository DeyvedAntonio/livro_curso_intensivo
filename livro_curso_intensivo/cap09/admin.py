from user import User
from privileges import Privileges

class Admin(User):
    """Classe criada para resolver o exercício 9.7."""
    
    def __init__(self, first_name, last_name, email, username, *privileges):
        """Inicializa os atributos da classe."""
        super().__init__(first_name, last_name, email, username)
        self.privileges = privileges


    # def show_privileges(self):
    #     """Lista o conjunto de privilégios de um administrador."""
    #     print(self.username, self.privileges)


admin_0 = Admin('Deyved', 'Silva', 'deyved@silva', 'D_S', 'can delete post', 'can ban user')
# admin_0.show_privileges()
admin_1 = Admin('Davi', 'Silva', 'davi@silva', 'D-S', 'can add post')
admin_1.privileges = Privileges('can delete post', 'can ban user')
admin_0.describe_user()
admin_1.describe_user()
admin_1.privileges.show_privileges()
