ultimo = 0
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Escolha um função\n[F] Final da Fila\n[A] Atendimento\n[S] Sair")
    operacao = input("Operação: ").upper()
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia ninguém para atender!")
    elif operacao == "F":
        ultimo += 1             # Adiciona um novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        print("Programa Finalizado co Sucesso!")
        break
    else:
        print("Operação inválida!\nDigite somente [F] - [A] ou [S]")
