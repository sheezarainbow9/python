# Listas:
# declarando uma lista vazia em Python
#lista1 = []

# criando lista
lista1 = [1, '2', 3]
#print(type(lista1), lista1)

# declaração explícita de lista
lista2 = list((1, '2', 3))
#print(lista2)

# declaração implícita de lista
lista3 = ['C', 4.65, True, 'True', 'Vamos aprender', ['outra', 'lista', 'interna'], lista2]
#print(lista3)

lista4 = ['primeiro', 'segundo', 'terceiro']
#print(lista4)

# acessando um elemento da lista
#print(lista3)
#print('')
#print(lista3[5][0]) # acessando lista dentro da lista

# fatiando listas:
# nomeDaLista[start:stop:step]
# execute um print por vez!
print(lista3)
print('')
print(lista3[2:6:2])
print('')
print(lista3[:3])
print('')
print(lista3[-1:])
print('')
print('Imprimindo de 2 em 2: ', lista3[::2])
print('')
print(lista3[: :]) # imprime a lista normal
print('')
print(len(lista3[5][2])) # imprime a quantidade de caracteres do 2° elemento da lista dentro da lista
print('')