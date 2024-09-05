menu = """

================= MENU =================

[1] - Depositar

[2] - Sacar

[3] - Extrato

[4] - Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        deposito = float(input("Insira o valor que deseja depositar: "))
        if deposito <= 0:
            print("Insira um valor válido.")
        else:
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
            saldo += deposito
            print(f"Saldo atual: R$ {saldo:.2f}")
            extrato += f"Depósito de R$ {deposito:.2f} efetuado\n"
            
            
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == 4:
        break
        
    else:
        print("Opção invalida. Escolha uma opção de 1 a 4.")