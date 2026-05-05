class Select:
    def by_id(self) -> any:
        print("Selecionando um elemento no BD")

class Insert:
    def inser_value(self) -> None:
        print("Inserindo um valor no BD")

class Repositorio:
    def __init__(self) -> None:
        self.__select = Select()
        self.__insert = Insert()
        #servem de elemento na composição de outra classe
        #COMPOSIÇÃO

    def select_by_id(self, id: int) -> any:
        self.__select.by_id()


repo = Repositorio()
repo.select_by_id(45)