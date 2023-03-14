# O 'self' indica que pertence à classe 'Pessoa'.

class Pessoa:
    def __init__(self, nome, idade, distancia):
        self.nome = nome
        self.idade = idade
        self.distancia = distancia

    # def apresentar(self):
    #     print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

    def aniversario(self):
      self.idade += 1

    def passos(self):
        self.distancia 
        

pessoa = Pessoa('Maria', 36, 5)
pessoa.aniversario()
pessoa.passos()

pessoa2 = Pessoa('João', 40, 6)
pessoa2.aniversario()
pessoa2.passos()

print(f'{pessoa2.nome} tem {pessoa2.idade} anos e {pessoa.nome} tem {pessoa.idade}.')
print(f'{pessoa2.nome} andou {pessoa2.distancia}km hoje.')
print(f'{pessoa.nome} andou {pessoa.distancia}km hoje.')
