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
# numeros = [1, 2, 3, 4, 5]
# pares = []
# for num in numeros:
#   if num % 2 == 0:
#     pares.append(num)

# print(f'Os números pares são {pares}.')

# While:

# produto = 0
# while produto < 4:
#     p = str(input('Digite o nome do produto: '))
#     v = float(input('Digite o valor do produto: R$ '))
#     produto += 1

# fruta = []
# valor = []
# while True:
#   fruta.append(str(input('Digite o nome fruta: ')))
#   valor.append(float(input('Digite o valor: R$ ')))
#   condition = str(input('Deseja continuar? (s/n) ')).lower()
#   if condition == 'n':
#     break

# print(f'Fruta: {fruta}\nValor: {valor}')

# percorrendo lista de números
# elemento = 0
# while elemento <= len([1, 2, 3, 4, 5, 6]):
#   print(f'Estamos no elemento: {elemento}')
#   elemento += 1

# percorrendo uma string
# s = 'STRING'
# indice = 0
# while indice in range(len(s)):
#   print(f'Estamos no elemento: {s[indice]}')
#   indice += 1

# jogo de adivinhação
# num_secreto = 42
# palpite = None
# while palpite != num_secreto:
#   palpite = int(input('Adivinhe o número: '))
#   if palpite < num_secreto:
#     print('Tente um número maior!')
#   elif palpite > num_secreto:
#     print('Tente um número menor!')

# print('Parabéns, você acertou!')

# i = 1
# while i <= 10:
#   if i == 5:
#     break
#   print(i)
#   i += 1

# i = 1
# while i < 5:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# enumerate (cria índice):

# palavra = 'tranquilo'
# for indice, letra in enumerate(palavra):
#   print(indice, letra)

l1 = ['eat', 'sleep', 'repeat']
s1 = 'geek'

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print(f'Return type: {obj1}')
print(list(enumerate(l1)))
print(list(enumerate(s1, 2)))
