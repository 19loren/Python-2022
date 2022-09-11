# Exercício 1:

numero = int(input('Insira um número inteiro: '))
def fatorial(numero): 
    fat = 1
    for contador in range(numero, 0, -1):
        fat *= contador
    return fat

print("O fatorial de ",numero,"é ", fatorial(numero)) 

# O exercicio 2 e 3 não consegui fazer
# Exercício 4:

def perfeito(numero):
    soma = 0
    for valor in range (1, numero):
         if numero % valor == 0:
            soma += valor
    if soma == numero:
        return True
    else:
        return False

def pft():
    numero = int(input("Entre com um número: "))
    if perfeito(numero) == True:
        print('O número inserido é perfeito')
    else:
        print('O número inserido não é perfeito')

pft()