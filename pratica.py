# palavra = str(input('Digite uma palavra: '))
# print(f'A palavra {palavra} tem {len(palavra)} letras.')

# frase = str(input('Digite uma frase: ')).upper()
# print(f'A letra "a" apareceu {frase.count("A")} vezes na frase digitada.')

# palavra = str(input('Digite uma palavra: ')).upper().replace(' ', '')

# if palavra == palavra[:: -1]:
#     print(f'A palavra {palavra} é um Palíndromo.')
# else:
#     print(f'A palavra {palavra} não é um Palíndromo.')


# frase = str(input('Digite um frase: ')).upper()

# print(f'A frase ao contrário fica: {frase[:: -1]}.')

# palavra = str(input('Digite algo: '))
# if palavra.isupper():
#     print(f'A palavra {palavra} contém apenas letras maiúsculas.')
# elif palavra.islower():
#     print(f'A palavra {palavra} contém apenas letras minúsculas.')
# else:
#     print(f'A palavra {palavra} contém letras maiúsculas e minúsculas.')


# palavra = str(input('Digite algo: ')).lower()
# vogais = ['a', 'e', 'i', 'o', 'u']

# for i in range(len(palavra)):
#     if palavra[i] in vogais:
#         palavra = palavra.replace(palavra[i], ' ')

# print(palavra)

frase = str(input('Digite uma frase: '))

nova_frase = [nova.lower() for nova in frase.split()]
nova_frase.sort()
print(nova_frase)