from cart import Cart

class User(Cart):
    def __init__(self, name:str, age:int, email:str, saldo:float, senha:str, back_account:str, items=None, tot_price=0):
        self.name = name
        self.age = age
        self.email = email
        self.__saldo = saldo
        self.__senha = senha
        self.__bank_account = bank_account
        super.__init__(items, tot_price)

    def setSenha(self, senha_antiga, senha_nova):
        if senha_antiga == self.__senha:
            self.__senha = senha_nova
            return True

        return False

    def setBankAccount(self, senha, nova_conta):
        if senha == self.__senha:
            self.__bank_account = nova_conta
            return True
        return False

    def getBankAccount(self, senha):
        if senha == self.__senha:
            return self.__bank_account
        return False

    def pagar(self, senha):
        if senha == self.__senha and self.tot_price < self.__saldo:
            self.__saldo -= self.tot_price
            return True
        return False
