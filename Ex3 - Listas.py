#Faça um Programa que peça as quatro notas de 10 alunos
#Calcule e armazene num vetor a média de cada aluno
#Imprima o número de alunos com média maior ou igual a 7.0

from itertools import count


ALUNOS = 2
NOTAS = 4
listaAluno = []
listaNota = []
listaMedia = []

media = 0

for i in range(ALUNOS):
    alunos = str(input('Digite o nome do aluno: \n'))
    listaAluno.append(alunos)
    for x in range(NOTAS):
        notas = float(input('Digite as notas: \n'))
        listaNota.append(notas)
        media += listaNota[i]
    media = media/4
    listaMedia.append(media)

aprovado = 0
for j in listaMedia:
    if j >= 7:
        aprovado += 1  

print(listaAluno)
print(listaMedia)
print(f'Há {aprovado} alunos com media acima de 7')
