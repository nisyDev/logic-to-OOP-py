class MinhaClasse:
    def __init(self) -> None:
        self.__Valor = None
        self.__elem = None

    def setter(self, valor: int) -> None:
        self.__Valor = valor

    def getter(self) -> int:
        return self.__Valor

my_class = MinhaClasse()
my_class.__Valor = 3 #Ferindo o Encapsulamento
print(my_class.__Valor)