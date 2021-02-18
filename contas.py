class Conta:
    def __init__(self,clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
        
    def resumo(self):
        print(f"CC Número: {self.numero} Saldo: {self.saldo:10.2f}")
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Valor maior que o saldo!")
            resp = int(input("Deseja continuar a operação?\n[1]-SIM\n[2]-NÃO:\n -> "))
            if resp == 1:
                self.saldo -= valor
                self.operacoes.append(["SAQUE", valor])
            elif resp == 2:
                print("Operação FINALIZADA!")
            else:
                print("Opção Inválida!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n\tSaldo: {self.saldo:10.2f}\n")
