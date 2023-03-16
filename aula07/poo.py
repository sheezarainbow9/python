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
        self.__cor = cor
        self.__ano = ano

    def get_idade(self):
        return self.__ano

    def set_idade(self, novo_ano):
        self.__ano = novo_ano
    
    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor


# class Nome(Carro):
#     def idade(self):
#         super().idade()


# class Utilidade(Carro):
#     def tipo(self):
#         super().tipo()


carro1 = Carro('verde', 2015)
print(carro1.get_cor())
carro1.set_cor('azul')
print(carro1.get_cor())  

# carro2 = Utilidade('azul', 2020)
# carro2.tipo()
# carro2.idade()
