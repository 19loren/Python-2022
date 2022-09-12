##Exercício Triângulo APPC

print('Programa testador de triângulos. Informe:')

va = int(input('Vértice A:'))
vb = int(input('Vértice B:'))
vc = int(input('Vértice C:'))

if (va + vb > vc) and (va + vc > vb) and (vb + vc > va):
    print('Esses valores formam um triângulo.')
else:
    print('Não é possível formar triangulo com esses valores.')
if (va == vb) and (va == vc) and (vb == vc):
    print('Este é um triângulo equilátero.')
elif (va != vb) and (va != vc) and (vb != vc):
    print('Este é um triângulo escaleno.')
else: 
    print('Este é um triângulo isósceles.')