#Cria uma função que dobra os valores de uma lista
def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 5, 2, 0, 1]
dobra(valores)
print(valores)