class ClasseQualquer:
    def fazer(self) -> None:
        print("Estou fazendo algo")

class OutraCoisa:
    def preparar(self) -> None:
        print("Estou preparando algo")

    #def fazer(self) -> None:
    #    print("Estou fazendo outra coisa")

def fazer_func() -> None:
    print("Estou fazendo outra coisa")

obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj2.fazer = fazer_func

obj1.fazer()
obj2.fazer()

#polimorfismo é este tipo de comportamento
#troca de dois métodos aparentemente iguais, mas se comportam de forma diferente
#básico
#porém, não é muito recomendado, pois pode ficar confuso e redundante