class Pessoa:
  def __init__(self,nome, idade) -> None:
    self.__nome = nome
    self._idade = idade

  def apresentar(self):
    print(f'Oi, meu nome é {self.__nome} e tenho {self._idade} anos.')


p = Pessoa('Alice', 25)
p.apresentar()
print(p.__nome)