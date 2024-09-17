from backend.products import Product
from backend.cashier import General

# Exemplo de produtos
products = [Product("Carro 0", 30000), Product("Louça", 200), Product("Brinquedo Hotweels", 1000)]

if __name__ == "__main__":
    accounts = []
    current_account = None
    option = 1

    while option != 0:
        print("Bem vindo ao supermercado do Baesse! :D")
        option = int(input("Digite a sua opção ([0] Sair [1] Logar, [2] Adicionar ao Carrinho, [3] Criar Conta, [4] Finalizar compra) "))
        
        match option:            
            case 1:
                username_or_email = input("Digite o nome do usuário ou email: ")
                password = input("Digite sua senha: ")

                if not accounts:
                    print("Ainda não temos contas registradas!")

                else:
                    for account in accounts:
                        if account.autenticate(username_or_email, senha):
                            print("Logado com sucesso!")
                            current_account = account
                        
                        else:
                            print("Credenciais incorretas!")

            case 2:
                pass

            case 3:
                username=input("Digite o nome de usuário: ")
                age=int(input("Informe a sua idade: "))
                email = input("Informe o seu email: "),
                saldo = float(input("Informe o seu saldo: "))
                senha = input("Crie a sua senha: ")
                conf = input("Confirme a sua senha: ")
                
                while conf != senha:
                    print("Senhas não convergem!")
                    conf = input("Confirme a sua senha: ")

                bank_account=input("Informe o seu banco: ")
                # Criação da instância da classe
                accounts.append(General(username=username, age=age, email=email, saldo=saldo, senha=senha, bank_account=bank_account))
                print("Conta Logada com sucesso!")
