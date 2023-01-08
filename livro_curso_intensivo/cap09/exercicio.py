from restaurant import Restaurant
from user import User, Privileges, Admin

restaurante = Restaurant('Novo', 'Mexicana')
restaurante.describe_restaurant()

admin_0 = Admin('Deyved', 'Silva', 'deyved@silva', 'D_S', 'can delete post', 'can ban user')
# admin_0.show_privileges()
admin_1 = Admin('Davi', 'Silva', 'davi@silva', 'D-S', 'can add post')
admin_1.privileges = Privileges('can delete post', 'can ban user')
admin_0.describe_user()
admin_1.describe_user()
admin_1.privileges.show_privileges()


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

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)