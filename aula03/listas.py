# Listas:
# declarando uma lista vazia em Python
#lista1 = []

# criando lista
#lista1 = [1, '2', 3]
#print(type(lista1), lista1)

# declaração explícita de lista
#lista2 = list((1, '2', 3))
#print(lista2)

# declaração implícita de lista
#lista3 = ['C', 4.65, True, 'True', 'Vamos aprender', ['outra', 'lista', 'interna'], lista2]
#print(lista3)

#lista4 = ['primeiro', 'segundo', 'terceiro']
#print(lista4)

# acessando um elemento da lista
#print(lista3)
#print('')
#print(lista3[5][0]) # acessando lista dentro da lista

# fatiando listas:
# nomeDaLista[start:stop:step]
# execute um print por vez!
# print(lista3)
# print('')
# print(lista3[2:6:2])
# print('')
# print(lista3[:3])
# print('')
# print(lista3[-1:])
# print('')
# print('Imprimindo de 2 em 2: ', lista3[::2])
# print('')
# print(lista3[: :]) # imprime a lista normal
# print('')
# print(len(lista3[5][2])) # imprime a quantidade de caracteres do 2° elemento da lista dentro da lista
# print('')
# print(lista3[::-1]) # imprime ao contrário

# adicionando elementos em numa lista
# print(lista1)
# lista1.append('Python')
# lista1.append('Java')
# lista1.append('Php')
# lista1.append('C#')
# print(lista1)

# inserir elementos em uma posição específica
# lista1.insert(2, 'C++') # vai inserir no segundo índice[2]
# print(lista1)

# remover um elemento pelo seu valor
# lista1.remove('Java')
# print(lista1)

# indexação (pegar um índice de um elemento pelo valor(nome))
# indice = lista1.index('2')
# print(indice)

# remover um elemento pelo seu índice
# del(lista1[indice])
# print(lista1)

# invertendo uma lista
# print('Lista original: ', lista4)
# lista4.reverse()
# print('lista invertida: ', lista4)

# ordenando uma lista
# lista4.sort()
# print('Lista ordenada: ', lista4)

# # comprimento de uma lista
# print(lista4, len(lista4), 'elementos')

# copia de lista
# l = [6, 7, 8, 9, 5]
# v=l
# print(v)
# print(l)

# testando se é mesmo cópia
# v[0] = -100
# print(v)
# print(l)

# forma correta de copiar listas
# l = [6, 7, 8, 9, 5]
# v = l[:2]
# z = list(l)
# print(l, v, z)

# exercícios:
# minhaLista = [76, 92.3, 'oi', True, 4, 76]
# minhaLista.append('pera')
# minhaLista.append(76)
# minhaLista.insert(3, 'gato')
# minhaLista.insert(0, 99)
# print(minhaLista.index('oi'))
# minhaLista.remove(True)

# print(minhaLista)