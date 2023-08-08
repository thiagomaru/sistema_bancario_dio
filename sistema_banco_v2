import textwrap

def menu():
  menu = """\n
  _________MENU_________
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar Contas
  [nu]\tNovo Usuário
  [q]\tSair
  _______________________
  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
      saldo+=valor
      extrato+=f"Deposito:\tR$ {valor:.2f}\n"
      print("\n__Deposito realizado com sucesso__")
    else:
      print("\nxxx A operação falhou! valor inválido! xxx")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
      print("\nxxx A operação falhou! Sem saldo suficiente. xxx")
    elif excedeu_limite:
      print("\nxxx A operação falhou! valor de saque excedido. xxx")
    elif excedeu_saques:
       print("\nxxx A operação falhou! número maximo de saques excedido xxx")
    elif valor > 0:
      saldo -= valor
      extrato += f"Saque:\t\"R$ {valor:.2f}\n"
      print("\n__ Saque realizado com sucesso! __")
    else:
      print("\nxxx A operação falhou! valor informado é invalido xxx")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato,):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print("\nxxx Já existe usuario com esse cpf! xxx")
      return

    nome = input("informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço de sua residencia: ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("__ usuario criado com sucesso__")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n___ Conta Criada com Sucesso! __")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nxxx Usuário não encontrado xxx")

def listar_contas(contas):
    for contas in contas:
        linha = f"""\
            Agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  while True:

    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Informe o valor de depósito:"))
      saldo, extrato = depositar(saldo, valor, extrato)


    elif opcao == "s":
      valor= float(input("Informe o valor de saque:"))

      saldo, extrato = sacar(
          saldo=saldo,
          valor=valor,
          extrato=extrato,
          limite=limite,
          numero_saques=numero_saques,
          limite_saques=LIMITE_SAQUES,

      )

    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      numero_conta = len(contas) + 1

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
      break

    else:
      print("Operação invalida! Por favor selecione novamete a operação desejada.")

main()
