class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f"O {self.tipo} esta apresentando seu show")



class Circo:
    def apresentar(self, artista: Artista) -> None:
        print("O circo está abrindo!")
        artista.apresentar_show()
        print("O público aplaude")
        
        
        #if command == 1:
         #   self.__show_palhaço()
        #if command == 2:
         #   self.__show_malabarista()

    #def __show_palhaço(self):
     #   print("O palhaço está apresentando seu show")

    #def __show_malabarista(self):
     #   print("O malabarista esta apresentando seu show")


circo = Circo()
palhaço = Artista("palhaço")
magico = Artista("magico")