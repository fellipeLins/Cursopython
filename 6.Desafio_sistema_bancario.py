# Deposito, saque, extrato
# 3 saques no valor de R$ 500,00, cso não tenha saldo informar que não tem saldo

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        
        else:
            print("Operacao falhou, o valor informado é invalido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Você excedeu o limite diário para saque.")
        
        elif excedeu_saques:
            print("Operação falhou, Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        
        else: 
            print("Operacao falhou, o valor informado é invalido.")
                
    elif opcao == "e":
        print("\n=================Extrato=================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "q":
        break

    else:
        print("Opcao Invalida, por favor selecione a opcao desejada.")