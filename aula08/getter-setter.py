class Pessoa:
  def __init__(self,nome, idade):
    self.__nome = nome
    self.__idade = idade

  def get_nome(self):
    return self.__nome

  def set_nome(self, novo_nome):
    self.__nome = novo_nome

  def get_idade(self):
    return self.__idade

  def set_idade(self, nova_idade):
    self.__idade = nova_idade


p = Pessoa('Alice', 25)   
print(p.get_nome())       # Obtendo o nome através do método get()
p.set_nome('Bob')         # Alterando o valor do nome através do método set()
print(p.get_nome())       # Verificando o novo nome através do método get()
