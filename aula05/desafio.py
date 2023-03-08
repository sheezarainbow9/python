titular = ''
conta = ''
saldo_conta = 0
saldo_poupanca = 0
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

    if opcao == 0:
        titular = str(input('Digite seu nome: '))
        conta = str(input('Digite o número da sua conta (3 dígitos): '))
        deposito = float(input('Efetue um depósito para criar uma conta: R$ '))
        saldo_conta += deposito
        if saldo_conta == 0 or saldo_conta == '':
            print('Conta não criada.')
        else:
            print('-' * 50)
            print(
                f'Nome: {titular}\nConta: {conta}\nValor do depósito: R$ {saldo_conta}\nConta criada com sucesso!')
