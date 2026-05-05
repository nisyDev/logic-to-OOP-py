class MinhaClasse:
    estatico = "lhama"
    #consigo criar um estático e mostrar ele sem precisar declarar um objeto
    
    def __init__(self, estado):
        self.estado = estado
        print(self)

obj = MinhaClasse(True)
obj2 = MinhaClasse(True)
obj3 = MinhaClasse(True)