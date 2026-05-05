class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f"O animal está andando pelo {self.localizacao}")

#uma classe se relaciona com a outra a partir de sua Herança
#este é um comportamento de heranças
class Cachorro(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)
        #vai chamar o init da classe superior

    def latir(self) -> None:
        print("O animal está latindo")
        self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print("O gato está miando")

dog = Cachorro("Brasil")
dog.latir()

cat = Gato("Noruega")
cat.miar()