titular = dict()
saldo_conta = 0
opcao = ''

while opcao != 4:
    print('=' * 30)
    print('BEM VINDA(O) AO BANCO FUCTURA!')
    print('=' * 30)
    print('ESCOLHA SUA OPÇÃO:')
    print('''
  0 - CRIAR CONTA
  1 - VERIFICAR SALDO
  2 - DEPOSITAR
  3 - SACAR
  4 - SAIR''')
    print('-' * 30)

    opcao = int(input('Qual a sua opção? '))
    print('=' * 30)

    if opcao == 0:
        print('CADASTRO DE CLIENTE')
        print('-' * 30)
        titular['nome'] = str(input('Digite seu nome: '))
        titular['conta'] = str(input('Digite o número da sua conta: '))
        titular['saldo'] = float(
            input('Efetue um depósito para criar uma conta: R$ '))
        saldo_conta += titular['saldo']
        if saldo_conta == 0 or saldo_conta == '':
            print('Conta não criada.')
        else:
            print('-' * 30)
            print('Conta criada com sucesso!')

    elif (opcao == 1):
        if (titular != ""):
            print("+--------------------------------------------------+")
            print("DADOS DA CONTA CORRENTE")
            print("+--------------------------------------------------+")
            print(titular)

    elif (opcao == 2):
        if (titular != ""):
            deposito = float(input("Valor do depósito: "))
            print('-' * 30)
            titular['saldo'] += deposito
            print("Depósito efetuado com sucesso!")

    elif (opcao == 3):
        if (titular != ""):
            valor_saque = float(input("Valor do saque: R$ "))
        if (valor_saque <= titular['saldo']):
            titular['saldo'] -= valor_saque
            print("Saque efetuado com sucesso!")
        else:
            print("Saldo insuficiente!")
            print("Seu saldo é R$", titular['saldo'])

    else:
        print("O Banco Fuctura agradece a preferência!")
