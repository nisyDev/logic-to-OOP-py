class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

        def enviar_mensagem(self, mensagem: str) -> None:
            print(f"enviando mensagem: {mensagem}")

        def abrir_emails(self) -> None:
            print("Abrindo os emails...")

        def abrindo_youtube(self) -> None:
            print("Abrindo YouTube...")

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.celular = celular

    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("Definindo o sabor...")
        self.celular.enviar_mensagem("Quero uma de calabreza")
        print("Aguardando a chegada")

android = Celular("Samsung")


#injeção de dependência = uma classe se relacionando com a outra a partir de nosso método construtor