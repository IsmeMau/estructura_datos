class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful.")
        else:
            print("Incorrect credentials.")

class Admin(User):
    def manageUsers(self):
        print(f"The admin {self.username} is managing users.")

class Customer(User):
    def makePurchase(self):
        print(f"The customer {self.username} is making a purchase.")
