
from user_module import User
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to ban users"]
    def show_privileges(self):
        print("Привілеї:", self.privileges)
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priv = Privileges()
