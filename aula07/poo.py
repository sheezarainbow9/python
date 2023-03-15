# class Animal:
#   def __init__(self, nome):
#     self.nome = nome

#   def fazer_som(self):
#     pass

# class Cachorro(Animal):
#   def fazer_som(self):
#     print(f'{self.nome} diz: Au, au!')

# class Gato(Animal):
#   def fazer_som(self):
#     print(f'{self.nome} diz: Miau!')

# class Pato(Animal):
#   def fazer_som(self):
#     print(f'{self.nome} diz: Quack!')

# cachorro1 = Cachorro('Rex')
# cachorro1.fazer_som()

# gato1 = Gato('Tom')
# gato1.fazer_som()

# pato1 = Pato('Donald')
# pato1.fazer_som()

class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano

    def idade(self):
        pass

    def tipo(self):
        pass


class Nome(Carro):
    def idade(self):
        print(
            f'O carro da cor {self.cor} é do ano de {self.ano}.')

class Utilidade(Carro):
    def tipo(self):
        print(
            f'O carro da cor {self.cor}, do ano de {self.ano} é um utilitário.')

carro1 = Nome('verde', 2015)
carro1.tipo()
carro1.idade()

carro2 = Utilidade('azul', 2020)
carro2.tipo()
carro2.idade()