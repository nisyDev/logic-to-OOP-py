from abc import ABC, abstractmethod

class ElementoInterface:

    @abstractmethod
    def executar(self) -> None: pass