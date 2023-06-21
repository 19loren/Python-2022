##Aula 2 - APPC

nome = input("Digite seu nome completo:\n")
print("O tamanho do seu nome em caracteres é: ", len(nome))
import sys
sys.getsizeof(nome)
print("Seu nome ocupa ", sys.getsizeof(nome), "bytes")