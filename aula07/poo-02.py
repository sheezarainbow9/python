# Super() -> traz os métodos da classe pai para a classe filho (herança).

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def fazer_som(self):
        print(f'{self.nome} faz bibi!')

class Fusca(Carro):
  def fazer(self):
    super().fazer_som()

teste = Fusca('Bob')
teste.fazer()