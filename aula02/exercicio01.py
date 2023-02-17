# Um cliente irá solicitar um empréstimo ao banco. Se o valor do empréstimo for menor ou igual a 50 % do seu salário, então o empréstimo será aprovado. Senão, se o valor do empréstimo for menor ou igual a 75 % do salário a situação ficará em análise. Senão, informe ao cliente que o empréstimo não foi aprovado. (ações: 1 – aprovar o empréstimo,  2 – situação em análise, 3 – não aprovar o empréstimo).


valor = float(input('Digite o valor do empréstimo: R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
metade = salario * 0.5
menorIgual = salario * 0.75

if (valor <= metade):
    print('Empréstimo aprovado!')
elif (valor <= menorIgual):
    print('Situação do empréstimo em análise...')
else:
    print('Empréstimo não aprovado.')
