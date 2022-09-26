#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes. 
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
#E depois informe o nome, os saltos e a média dos saltos. 
#O programa deve ser encerrado quando não for informado o nome do atleta. 

listaSalto = []

nome = str(input('Digite o nome do atleta: '))

listaSalto.append(float(input('Primeiro salto:\n ')))
listaSalto.append(float(input('Segundo salto:\n ')))
listaSalto.append(float(input('Terceiro salto:\n ')))
listaSalto.append(float(input('Quarto salto:\n ')))
listaSalto.append(float(input('Quinto salto:\n ')))

somaSaltos = 0
media = 0
for i in listaSalto:
    somaSaltos += i

media = somaSaltos / 5

print(f'Atleta:' + nome)
print('Saltos:')
print(listaSalto)
print('Média dos saltos:')
print(media)







