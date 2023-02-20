# Atividades da aula 02:

# 1. Faça um programa que leia um número inteiro e
# verifique se ele é um número primo. Um número é
# primo se ele é divisível apenas por 1 e por ele mesmo.
# Se o número for primo, o programa deve imprimir "É um
# número primo", caso contrário, deve imprimir "Não é um número primo".

# num = int(input('Digite um número: '))
# cont = 0

# for i in range(1, num+1):
#   if num % i == 0:
#     cont+=1

# if cont == 2:
#   print(f"O número {num} é primo.")
# else:
#   print(f"O número {num} não é primo.")


# 2 - Escreva um programa que recebe o nome e
# a idade de uma pessoa e verifica se ela pode votar nas eleições.

# nome = str(input('Digite o seu nome: '))
# idade = int(input('Digite a sua idade: '))

# if (idade >= 18) and (idade <= 64):
#     print(f'{nome} tem {idade} anos e pode votar.')
# elif (idade >= 16 and idade <= 17) or (idade >= 65):
#     print(f'{nome} tem {idade} anos e o voto é facultativo.')
# else:
#     print(f'{nome} ainda não pode votar.')


# 3 - Escreva um programa que recebe um número e retorna
# a sua raiz quadrada, caso o número seja positivo, e uma
# mensagem de erro, caso contrário.

# import math

# num = float(input('Digite um número: '))

# if num < 0:
#     print('Número negativo!')
# else:
#     raiz = math.sqrt(num)
#     print(f'\nA raiz quadrada de {num:.0f} é {raiz:.0f}.\n')


# 4 - Escreva um programa que recebe alguns números e retorna o maior número.

# lista = []

# for n in range(0, 4):
#     lista.append(int(input('Digite um número: ')))

# print (f'O maior número da lista é: {max(lista)}.')


# 5 - Escreva um programa que verifica se um número é par ou ímpar.

# num = int(input('Digite um número: '))

# if (num % 2 == 0):
#     print(f'O número {num} é par.')
# else:
#     print(f'O número {num} é ímpar.')


# 6 - Escreva um programa que verifica se um número
# é positivo, negativo ou zero.

# num = float(input('Digite um número: '))

# if (num < 0):
#     print('Número negativo.')
# elif (num > 0):
#     print('Número positivo.')
# else:
#     print('Número igual a zero.')


# 7 - Escreva um programa que calcula a média
# de dois números e retorna "Aprovado" se a
# média for maior ou igual a 7 e "Reprovado" caso contrário.

# nota1 = float(input('Digite a 1a nota: '))
# nota2 = float(input('Digite a 2a nota: '))

# if (nota1 + nota2 / 2 >= 7):
#     print('\nAprovada(o)!')
# else:
#     print('\nReprovada(o)!')


# 8 - Escreva um programa que recebe uma letra
# e verifica se é uma vogal ou uma consoante.

# letra = str(input('Digite uma letra: '))
# vogais = ['a', 'e', 'i', 'o', 'u']

# if (letra not in vogais):
#     print(f'"{letra}" é uma consoante.')
# else:
#     print(f'"{letra}" é uma vogal.')


# 9 - Faça um programa que receba dois valores inteiros
# e um operador aritmético (+, -, *, / ou %) e realize a
# operação correspondente. Se o operador for inválido, o
# programa deve imprimir "Operador inválido". O programa
# deve tratar os casos de divisão por zero e de valores
# inválidos para os operandos.

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))

operador = input(
    'Escolha o símbolo da operação a ser realizada:\n(+, -, *, /, %) - ')

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num1 == 0:
        resultado = 0
    else:
        resultado = num1 / num2
elif operador == "%":
    resultado = num1 % num2
else:
    print("Operação inválida! Tenta novamente.")
    resultado = 0
    
print(f'Resultado: {resultado:.0f}.')
