#Programa que peça a idade e a altura de 5 pessoas
#Armazene cada informação no seu respectivo vetor
# Imprima a idade e a altura na ordem inversa a ordem lida.

listaIdade = []
listaAltura = []

for i in range(3):
    idade =  int(input('Digite a idade: \n'))
    listaIdade.append(idade)
    altura = float(input('Digite a altura: \n'))
    listaAltura.append(altura)

listaIdade.reverse()
listaAltura.reverse()

print(listaIdade)
print(listaAltura)

