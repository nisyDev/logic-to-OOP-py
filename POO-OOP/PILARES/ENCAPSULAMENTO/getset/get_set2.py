class MinhaClasse:
    def __init(self) -> None:
        self.__Valor = None
        self.__elem = None

    def setter(self, valor: int) -> None: #esse int é para informar ao outro programador que o atributo do método seja inteiro, serve somente para comunicação
        self.__Valor = valor

    @property
    def getter(self) -> int:
        return self.__Valor

my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor)
