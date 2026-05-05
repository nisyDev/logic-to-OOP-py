class SistemaCadastral:

    def cadastrar(self, nome: str, cpf: int) -> None:
        if self.__validate_input(nome, cpf):
             self.__register_user(nome, cpf)
        else:
            self.__error_handle()

    def __validate_input(self, nome: str, cpf: int) -> bool:
        return isinstance(nome, str) and isinstance(cpf, int)
    
    def __register_user(self, nome: str, cpf: int) -> None:
            print("Acessando o banco de dados...") #2 responsabilidade
            print(f"Cadastrar usuário {nome}, idade {cpf}")

    def __error_handle(self) -> None:
        print("dados inválidos") #3 responsabilidade


