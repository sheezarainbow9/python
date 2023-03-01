# Dicionários:

# criando um dicionário vazio
# dicionario = {}

# criando um dicionário com alguns pares chave-valor
# dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'Recife'}
# print(dicionario)

# declarando dicionários
# dic = {}
# print(type(dic))
# dic_pernambuco = {'Sport': 41, 'Santa Cruz': 29, 'Náutico': 21}
# print(dic_pernambuco)

# adicionando um elemento no dicionário (chave:valor)
# onde a chave é Salgueiro e o valor é 1.
# note que a chave é passada dentro de colchetes, após o nome do dicionário.
# dic_pernambuco['Salgueiro'] = 1
# print(dic_pernambuco)

# remover um elemento com base na chave
# del dic_pernambuco['Salgueiro']
# print(dic_pernambuco)

# remove a chave e retorna seu valor
# valor = dic_pernambuco.pop('Náutico')
# print('O valor retornado da chave é: ', valor)
# print(dic_pernambuco)

# verificar se uma chave existe no dicionário
# print('Santa Cruz' in dic_pernambuco)

# removendo e retornando o último elemento
# dic_paulista = {'Corinthians': 29, 'Santos': 22, 'Palmeiras': 22}
# print(dic_paulista.popitem())
# print(dic_paulista)

# mesclar 2 dicionários
# dic_pernambuco.update(dic_paulista)
# print(dic_pernambuco)

# O que acontece em cada sequencia de comandos a seguir?
d = {'apples': 15, 'bananas': 35, 'grapes': 12}

# print(d['banana']) - erro, banana não existe no dic
        
# d['oranges'] = 20
# print(len(d)) - acrescenta oranges e dá quantos itens tem no dic (4)

# print( 'grapes' in d) - retorna True

# print(d['pears']) - erro, pears não existe no dic

# print(d.get('apples')) - retorna o valor da chave

# fruits = d.keys() - pega as chaves
# fruits.sort() - não existe este atributo
# print(fruits) - retorna os valores das chaves

# del d['apples']
# print('apples' in d) - deleta apples e retorna seu valor como False
