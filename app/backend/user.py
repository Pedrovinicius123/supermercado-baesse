from backend.cart import Cart

class User(Cart):
    def __init__(self, username:str, age:int, email:str, senha:str, items=[], tot_price=0):
        self.username = username
        self.age = age
        self.email = email
        super().__init__(tot_price)

    
    
