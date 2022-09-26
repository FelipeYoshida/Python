#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo
# E ‘N’, se seu argumento for zero ou negativo.

def numero(x):
    if x < 0:
        return 'N'
    elif x > 0:
        return 'P'
    else:
        return 'Zero'


print(numero(-8))