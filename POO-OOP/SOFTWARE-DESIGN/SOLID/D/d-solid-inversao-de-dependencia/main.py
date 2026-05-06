from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal:
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def main(self) -> None:
        self.__elem.executar()
        print("Estou finalizando na classe principal")

el = Elemento2()

cll = Principal(el) #estamos simplificando a relação da classe com o elemento
cll.main()