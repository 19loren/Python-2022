#Atividade Lucia - Luiza e Gabi 3

#Gabriela Ferreira Gomes 21926613
#Loren Severi Tavolaro 21012402
#Luiza Eduarda Limoli 22016388

#EX1:
# elabore um programa que leia um número inteiro e uma função que calcule seu fatorial

from configparser import Interpolation
from sqlite3 import IntegrityError


numero = int(input('Digite um número: ') )

resultado_fatorial = 1
for r in range(1, numero + 1):
    resultado_fatorial *= r

print(resultado_fatorial)

#EX3:
#elabore um programa que leia um número inteiro e construe duas funções: uma que some os dígitos desse número inteiro e outra
#que determine o maior dígito desse nùmero

quantidade_numeros = int(input('Quantos números: '))
primeiro_numero = int(input('Número 1: '))

maior_numero = primeiro_numero
soma_numeros = primeiro_numero
contador = 1 

while contador < quantidade_numeros:
    contador += 1
    maior_numero_inserido = int(input('Número %d: '%contador))
    #%d: formatação pra números
    
    soma_numeros += maior_numero_inserido
    
    if maior_numero_inserido > maior_numero:
        maior_numero = maior_numero_inserido

print('Soma dos números: ', soma_numeros)
print('Maior número: ', maior_numero)
