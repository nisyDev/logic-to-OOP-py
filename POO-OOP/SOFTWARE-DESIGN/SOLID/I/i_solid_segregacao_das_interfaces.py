#classe ela nao deve ser forcada a depender de uma interface que nao utiliza

from abc import ABC, abstractmethod

class Trabalhador(ABC): #interface -> uma pré assinatura uma construção de uma classe atuante

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def consultar_beneficios(self) -> None: pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor esta indo para casa")

    def consultar_beneficios(self) -> None:
        print("Consultar beneficios da CLT")

class ProfessorSubstituto(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor esta indo para casa")

        #def consultar_beneficios(self) -> None:
        #raise Exception("O Professor Substituto nao tem beneficios") #nao pode fazer uma situacao que já gere um erro (quebra de segregacao)
        #o professor nao vai utilizar consultar_beneficios

p2 = ProfessorSubstituto()