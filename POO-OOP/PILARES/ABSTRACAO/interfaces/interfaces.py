#nao existe em python uma entidade ou elemento que utilizemos em python que seja uma interface
#utilizamos classe e metodos abstratos para criarmos

from abc import ABC, abstractmethod

class Trabalhador(ABC): #interface -> uma pré assinatura uma construção de uma classe atuante

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoco(self) -> None: pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor esta indo para casa")

    def horario_de_almoco(self) -> None:
        print("O professor esta almocando")

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print("O engenheiro esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O engenheiro esta indo para casa")

    def horario_de_almoco(self) -> None:
        print("O engenheiro esta almocando")

def comunicar_o_trabalhador(trabalhador: Trabalhador): #posso colocar o trabalhador como int, float ou dict também, mas colocar trabalhador pode ser tipado desse jeito como interface do elemento
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir para a casa")
    trabalhador.ir_para_casa()


p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
print()

comunicar_o_trabalhador(p2)
print()

#implementação de interface