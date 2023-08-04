menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "d":
    valor = float(input("Informe o valor de depósito:"))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
      print("Operação falhou! Valor inválido!")

  
  elif opcao == "s":
    valor= float(input("Informe o valor de saque:"))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Operação Falhou! Sem Saldo Suficiente")
    elif excedeu_limite:
      print("Operação Falhou! Valor de saque excedido")
    elif excedeu_saques:
      print("Operação Falhou! Limite de saques excedido")
    elif valor>0:
      saldo-=valor
      extrato+= f"Saque: R$ {valor:.2f}\n"
      numero_saques+=1
    else:
      print("Operação Falhou! Valor Inválido") 


  elif opcao == "e":
    print("\n__________Extrato__________")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("___________________________")
    
  elif opcao == "q":
    break

  else:
    print("Operação invalida! Por favor selecione novamete a operação desejada.")
