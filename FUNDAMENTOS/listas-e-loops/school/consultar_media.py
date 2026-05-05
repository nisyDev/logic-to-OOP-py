print("Escola Estadual Dr. Fulano Ciclano Beltrano\n")
print("Sala 25 - 1º ano do ensino médio (turma B)\n\n")
print("Atenção: este sistema serve somente para calcular suas notas semestrais, em caso de dúvidas ou ocorrências entre em contato com a Secretaria, das 07h às 18h.\n\n")
print("Digite cada nota para calcular sua média total do semestre\n")

print("Português:")
notaPort = float(input())
print("Matemática:")
notaMat = float(input())
print("História:")
notaHis = float(input())
print("Biologia:")
notaBio = float(input())
print("Geografia:")
notaGeo = float(input())
print("Arte:")
notaArt = float(input())
print("Química:")
notaQuim = float(input())
print("Ed. Física:")
notaEdFis = float(input())
print("Linguagem Estrangeira:")
notaLing = float(input())



materias = [notaPort, notaMat, notaHis, notaBio, notaGeo, notaArt, notaQuim, notaEdFis, notaLing] #lista
pesos = [5, 5, 4, 4, 3, 3, 5, 1, 3] #coleção de notas
soma = 0
soma_pesos = 0
for i in range(len(materias)):
    soma = soma + (materias[i] * pesos[i])
    soma_pesos = soma_pesos + pesos[i]
media = soma / soma_pesos

print("\n\nCalculando...\n\n")

print(f"Sua média do semestre é: {media:.2f}")
