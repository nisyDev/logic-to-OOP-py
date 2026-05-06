#objetos podem ser substituídos pelos seus herdeiros sem que isso mude 

class Animal:
    def alimentar(self) -> None:
        print("O animal está se alimentando")

class Cachorro(Animal):
    def latir(self) -> None:
        print("O cachorro está latindo")

class Peixe(Animal):
    def nadar(self) -> None:
        print("O peixe esta nadando")

    def latir(self):
        raise Exception("Peixe nao late") #o método de latir vai levantar uma exceção
    
def verificar_animal(animal: Animal):
    animal.alimentar()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)