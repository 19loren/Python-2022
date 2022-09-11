#Recursão - Função Recursiva
def somatoria(n):
    if n == 1:
        return 1
    else:
        return n + somatoria(n-1)
if __name__ == '__main__':
    n = 1
    while n < 10:
        print("Bom dia: ", n)
        n = n + 1 

#Recursão é a chamada de uma função denro dela mesma


if __name__ == '__main__':
   n = int(input("Entre com o numero: "))
   if n > 0:
       somatoria = 0
       while n > 0:
           somatoria = somatoria + n
           n = n - 1
print('A somatória é: ', somatoria)

#

def somatoria(n):
    if n == 1:
        return 1
    else: 
        return n + somatoria(n - 1)

if __name__ == '__main__':
    x = int(input('somatoria de 1 ate: '))
    print("soma: ", somatoria(x))

#PG: EXEMPLO:
#PG iniciando em 2, de razão 2
#Resultado: 2, 4, 8, 16, 32..
#faca um programa q calcule uma razao geometrica, tamanho max = 5 numeros, pergunte numero inicial e a razao

if __name__ == '__main__':
    n = int(input("inicio da pg: "))
    r = int(input("razao: "))
    print(n)
    for i in range(1, 5):
        n = n * r 
        print(n)

# mesmo ex com while

if __name__ == '__main__':
    n = int(input("inicio da pg: "))
    r = int(input("razao: "))

    somatoria = 1 
    while somatoria < 5:
        n = n * r
        print(n)
        somatoria = somatoria + 1

