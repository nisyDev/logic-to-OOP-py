class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf
        #self.__cpf = cpf
        # também se aplica ao atributo

    def apresentar(self):
        print(f"Ola! Minha altura - {self.altura}")

    def coletar_documento(self):
        print(f"Meu documento - {self.cpf}")
    
    #def __coletar_documento(self):
    #   #print(f"Meu documento  - {self.cpf}"")
    # este método é privado, filtra informações e é incluído no processamento do método apresentar

jorge = Pessoa("1.70", "fdsjkhfsdkj")
jorge.apresentar()