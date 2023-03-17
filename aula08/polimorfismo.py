# Polimorfismo usa o mesmo método da classe pai trazendo ele para a classe filha modificando-o.

# class Animal:
#     def fazer_som(self):
#         pass


# class Cachorro(Animal):
#     def fazer_som(self):
#         print('Au au!')


# class Gato(Animal):
#     def fazer_som(self):
#         print('Miau!')


# animais = [Cachorro(), Gato()]
# for animal in animais:
#     animal.fazer_som()

# class Forma:
#     def area(self):
#         pass


# class Retangulo(Forma):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def area(self):
#         return self.largura * self.altura


# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio

#     def area(self):
#         return 3.14 * self.raio ** 2


# formas = [Retangulo(2, 3), Circulo(1)]
# for forma in formas:
#     print(forma.area())

class Forma:
    def __init__(self, largura, altura, raio):
        self.largura = largura
        self.altura = altura
        self.raio = raio
        
    def area(self):
      pass

class Retangulo(Forma):
    def area(self):
      return self.altura * self.largura

class Circulo(Forma):
  def area(self):
    return 3.14 * self.raio ** 2


r1 = Retangulo(1, 2, 3)
print(r1.area())

c1 = Circulo(3, 2, 1)
print(c1.area())


