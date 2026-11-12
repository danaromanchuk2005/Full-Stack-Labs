from user_models import User

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priv = Privileges()
