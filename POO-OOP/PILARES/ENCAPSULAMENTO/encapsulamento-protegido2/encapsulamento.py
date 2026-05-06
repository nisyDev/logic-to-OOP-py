class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f"O animal esta andando pelo {self.localizacao}")

    def __dormir(self) -> None: #Metodo protegido
        print("O animal esta dormindo")

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print("O gato está miando")
        self.__dormir()
        print(self._tamanho)


cat = Gato("Argentina")
cat.miar()
cat.__dormir() #deveria dar erro / elementos protegidos nao sao chamados por objetos
print(cat._tamanho) #elementos protegidos não são chamados por objetos, não é uma boa prática