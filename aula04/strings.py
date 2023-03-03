# Strings:

# declarando uma string
msg = 'Hello, World!'
print(msg)

# concatenando string
# primeiro_nome = 'João'
# sobrenome = 'Silva'
# print(primeiro_nome + ' ' + sobrenome)

# acessando caracteres individuais numa string
# primeiro_caractere = msg[0]
# ultimo_caractere = msg[-1]
# print(primeiro_caractere)
# print(ultimo_caractere)

# comprimento de uma string
# print(f'comprimento = ', len(msg))

# convertendo string para maiúsculas e minúsculas
# maiuscula = msg.upper()
# minuscula = msg.lower()
# print(maiuscula, minuscula)

# dividindo string em substring com base em um delimitador
# palavras = msg.split(',')
# print(palavras)

# verificando se uma substring está presente (ele vai considerar cada caractere, não a palavra exata)
#if 'World' in msg:
    #print('A substring "World" está presente na mensagem.')

# substituindo caracteres em uma string
# nova_msg = msg.replace('World', 'Python')
# print(nova_msg)

# formatando string
# nome = 'João'
# idade = 30
# print('Meu nome é {} e tenho {} anos.'.format(nome, idade))
# print(f'Meu nome é {nome} e tenho {idade} anos.')

# utilizando caracteres de escape numa string (pular linha)
# print('Eu gosto de programar em Python!\nEle é uma linguagem muito poderosa.')

# convertendo string em número
# num = '123'
# print('Inteiro:', int(num))
# print('Float:', float(num))

# acessando substring de uma string
#print(msg[0:5]) # retorna os 5 primeiros caracteres

# saltando caracteres durante fatiamento
# print('letras ímpares:', msg[1::2])

# usando fatiamento para reverter uma string
# print('reverso:', msg[::-1])

# removendo espaços em branco de uma string
msg1 = ' Hello, World! '
print(msg1.strip())