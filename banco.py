from contas import Conta
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
    
    def abrir_conta(self, conta):
        self.contas.append(conta)
    
    def listar_contas(self, conta):
        for c in self.contas:
            c = Conta()
            c.resumo()
