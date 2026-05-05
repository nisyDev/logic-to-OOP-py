class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco SQL")

class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")


class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")

class DBHandler(SqlRepository): #mas se trocasse para NoSQLRepository, não seria uma boa prática
    def alterTable(self):
        print("Alterando tabela em SQL")

    #Caso buscasse no NoSQL
    #def select(self):
    #    raise Exception("Não busca dados no banco NoSQL")


#sempre nas classes mais genéricas que herda as mais específicas