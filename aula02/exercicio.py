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

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))

if (idade >= 18) and (idade <= 64):
    print(f'{nome} tem {idade} anos e pode votar.')
elif (idade >= 16 and idade <= 17) or (idade >= 65):
    print(f'{nome} tem {idade} anos e o voto é facultativo.')
else:
    print(f'{nome} ainda não pode votar.')
