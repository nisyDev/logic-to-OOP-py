from abc import ABC, abstractmethod
#elemento abstrato

class Pessoa(ABC): #classe abstrata nao possui objetos - só pode herdar
    def correr(self):
        print("A pessoa esta correndo de manha")

    @abstractmethod # classe de herança DEVE criar um método trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("O profesor esta dando aula")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O cozinheiro esta cozinhando")

p1 = Professor()
p2 = Cozinheiro()
p1.trabalhar()
p1.correr()