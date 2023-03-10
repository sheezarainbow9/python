# def numeros(n):
#   for i in range(n):
#     i += 1
#     print(str(i) * i)

# n = int(input('Digite um número: '))
# numeros(n)

# def soma(a, b, c):
#     s = a + b + c
#     return s

# a = int(input('Digite o 1° número: '))
# b = int(input('Digite o 2° número: '))
# c = int(input('Digite o 3° número: '))

# print('A soma dos números =', soma(a, b, c))

# def positivo(n):
#   if n > 0:
#     print('P')
#   elif n == 0:
#     print('N')
#   else:
#     print('Z')

# positivo(int(input('Digite um número: ')))

# def somaImposto(taxaImposto, custo):
#   return (1 + taxaImposto/100) * custo

# taxa = float(input('Digite a taxa de imposto: '))
# custo = float(input('Digite o custo: R$ '))
# print(f'Valor com imposto: R${somaImposto(taxa, custo):.2f}')

def sequencia(numero):
  for numero in range(numero + 1):
    for n in range(1, numero + 1):
      print(f'{n}', end='')
    print()


numero = int(input('Digite um número: '))
sequencia(numero)
