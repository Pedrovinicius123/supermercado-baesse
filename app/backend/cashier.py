from backend.user import User

class General(User):
    def __init__(self, senha:str, username:str, age:int, email:str, saldo:float, bank_account:str, items=[], tot_price=0):
        self.__senha = senha
        self.__saldo = saldo
        self.__bank_account = bank_account

        super().__init__(username, age, email, tot_price)

    def autenticate(self, username_or_email:str, senha:str):
        if (username_or_email == self.email or username_or_email == self.username) and senha == self.__senha:
            return True
        return False

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

    def getSaldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        return False

    def pagar(self, senha):
        if senha == self.__senha and self.tot_price < self.__saldo:
            self.__saldo -= self.tot_price
            return True
        return False
