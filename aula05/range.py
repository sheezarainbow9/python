# Range:

# gerando uma sequência de 0 a 9
# print(list(range(10)))

# gerando uma sequência de 1 a 10
# print(list(range(1, 11)))

# gerando uma sequência de 0 a 30 com step 5
# print(list(range(0, 30, 5)))

# gerando uma sequência numérica negativa
# print(list(range(0, -10, -1)))

# Iteração e laços(repetição):

# for i in range(1, 6):
#   print(i)

# i = 1
# while i <= 5:
#   print(i)
#   i += 1

# For:
# produtos = []
# valores = []

# for i in range(0, 4):
#   p = str(input('Digite o nome do produto: '))
#   v = float(input('Digite o valor do produto: R$ '))
#   produtos.append(p)
#   valores.append(v)

# print(f'Produtos: {produtos}\nValores: {valores}')

# percorrendo lista de números
# for elemento in [1, 2, 3, 4, 5, 6]:
#   print('Estamos no elemento', elemento)

# percorrendo uma string
# for elemento in 'STRING':
  # print('Estamos no elemento', elemento)

# percorrendo os índices de uma string
# for elemento in range(len('STRING')):
#   print('Estamos no elemento', elemento)

# iterar sobre uma lista de números e calcular a soma
# numeros = [1, 2, 3, 4, 5]
# soma = 0
# for num in numeros:
#   soma += num

# print(f'A soma é {soma}.')

# iterar sobre uma string e contar o número de ocorrências
# texto = 'hello, world'
# contagem = 0
# for letra in texto:
#   if letra =='l':
#    contagem += 1
   
# print(f'A contagem de ocorrências da letra é {contagem}.')

# iterar sobre uma lista e filtrar os elementos pares
numeros = [1, 2, 3, 4, 5]
pares = []
for num in numeros:
  if num % 2 == 0:
    pares.append(num)

print(f'Os números pares são {pares}.')