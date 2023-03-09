# try:
#   vetor = list(range(4))
#   print('Antes da execução!')
#   print(vetor[4])
#   print('Este texto não será impresso!')
# except IndexError as error:
#   print('A quantidade de elementos solicitada é maior que o tamanho da lista.')

v1 = [4, 8, 16, 32, 64, 128]
v2 = [2, 0, 4, 8, 0]

# for i in range(len(v1)):
#   try:
#     div = v1[i]/v2[i]
#     print('%d / %d = %d' %(v1[i], v2[i], div))
#   except (ZeroDivisionError, IndexError):
#     print('Zero não é divisível; as listas tem tamanhos diferentes.')

for i in range(len(v1)):
  try:
    div = v1[i]/v2[i]
    print('%d / %d = %d' %(v1[i], v2[i], div))
  except:
    print('Deu erro.') # não é boa prática. tente saber o erro a ser tratado antes de usar.