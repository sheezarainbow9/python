# Escreva um programa que solicite ao usuário que digite uma palavra e exiba o comprimento da palavra.
# palavra = str(input('Digite uma palavra: '))
# print(f'A palavra {palavra} tem {len(palavra)} letras.')

# Escreva um programa que solicite ao usuário que digite uma frase e conte o número de ocorrências de uma determinada letra na frase.
# frase = str(input('Digite uma frase: ')).upper()
# print(f'A letra "a" apareceu {frase.count("A")} vezes na frase digitada.')

# Escreva um programa que solicite ao usuário que digite uma palavra e verifique se a palavra é um palíndromo (ou seja, se a palavra pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda).
# palavra = str(input('Digite uma palavra: ')).upper().replace(' ', '')

# if palavra == palavra[:: -1]:
#     print(f'A palavra {palavra} é um Palíndromo.')
# else:
#     print(f'A palavra {palavra} não é um Palíndromo.')

# Escreva um programa que solicite ao usuário que digite uma frase e exiba a frase com as palavras em ordem inversa.
# frase = str(input('Digite um frase: ')).upper()

# print(f'A frase ao contrário fica: {frase[:: -1]}.')

# Escreva um programa que solicite ao usuário que digite uma palavra e verifique se a palavra contém apenas letras maiúsculas, apenas letras minúsculas ou uma combinação de ambas.
# palavra = str(input('Digite algo: '))
# if palavra.isupper():
#     print(f'A palavra {palavra} contém apenas letras maiúsculas.')
# elif palavra.islower():
#     print(f'A palavra {palavra} contém apenas letras minúsculas.')
# else:
#     print(f'A palavra {palavra} contém letras maiúsculas e minúsculas.')

# Escreva um programa que solicite ao usuário que digite uma palavra e exiba a palavra sem vogais.
# palavra = str(input('Digite algo: ')).lower()
# vogais = ['a', 'e', 'i', 'o', 'u']

# for i in range(len(palavra)):
#     if palavra[i] in vogais:
#         palavra = palavra.replace(palavra[i], ' ')

# print(palavra)

# Escreva um programa que solicite ao usuário que digite uma frase e exiba a frase com as letras em ordem alfabética, ignorando espaços e pontuações.
# frase = str(input('Digite uma frase: '))

# nova_frase = [nova.lower() for nova in frase.split()]
# nova_frase.sort()
# print(f'A frase digitada em ordem alfabética nas palavras: {nova_frase}')

# Escreva um programa que solicite ao usuário que digite uma palavra e exiba a palavra com as letras em ordem alfabética.
# palavra = str(input("Digite uma palavra: ")).upper()
# lista = list(palavra)
# lista_ordenada = sorted(lista)

# print(f'A palavra digitada em ordem alfabética das letras: {lista_ordenada}')
