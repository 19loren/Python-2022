##Exercício Repetição - APPC-P

##measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

##criar uma lista com range de 5 a 50 inclusive o 50 (5 a 51), percorrer essa lista com o for e imprimir todos os numeros pares

numeros = list(range(5, 51))
for n in numeros:
    if (n % 2 == 0):
     print(n)

##num range(1,11) calcular o quadrado de todos os numeros que aparecer e imprimir na tela

for r in range(1, 11):
    print(r * r)

##usando pow -> ele nao devolve numero inteiro, devolve float
import math
for r in range(1, 11):
    print(math.pow(r, 2))

##se o numero for par, potencia ao quadrado, se for impar, potencia ao cubo

import math
for r in range(1, 11):
    if r % 2 == 0:
        ##por ter so uma condicao a ser testada, nao precisa de parenteses
        print(math.pow(r, 2))
    else:
        print(math.pow(r, 3))

##segundo modo com duas repeticoes:

for r in range(2, 10):
    for x in range(2, n):
        if r % x == 0:
            print(r, 'equals', x, 's', r//x)
            break
        else:
            #loop fell through without finding a factor
            print(r, 'is a prime number')