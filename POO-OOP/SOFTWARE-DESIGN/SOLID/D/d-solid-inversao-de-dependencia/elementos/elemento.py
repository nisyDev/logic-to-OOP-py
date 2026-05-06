#boa utilizacao de interface 
from elementos.interfaces.elemento_interface import ElementoInterface

class Elemento(ElementoInterface):
    def executar(self) -> None:
        print("Estou executando o elemento")