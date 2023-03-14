# O 'self' indica que pertence à classe 'Pessoa'.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # def apresentar(self):
    #     print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

    def aniversario(self):
      self.idade += 1

pessoa = Pessoa('Maria', 36)
pessoa.aniversario()

pessoa2 = Pessoa('João', 40)
pessoa2.aniversario()

print(f'{pessoa2.nome} tem {pessoa2.idade} anos e {pessoa.nome} tem {pessoa.idade}.')
