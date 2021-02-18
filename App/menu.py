from contas import Conta
from cliente import Cliente

class Menu:

    print("#-" * 20) 
    print("\tBem vindo ao Banco Pi")
    print("#-" * 20)

    def __init__(self):
        print("\n[1] Cadastrar Conta\t[2] Verificar Extrato\n[3] Saque\t\t[4] Depósito\n[5] Sair")
        self.op1 = int(input("\nSelecione uma opção: "))

        if self.op1 == 1:
            c = Cliente()
            print("Cliente cadastrado com sucesso!")
        elif self.op1 == 2:
            conta = Conta()
            conta.extrato()
m = Menu()
