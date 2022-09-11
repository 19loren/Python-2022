##match APPC-P
#supondo que sua nota final vale de 0 a 10, 0 a 4 = reprovado e quantos pontos faltam pra aprovar, fazer tambem com 5 a 10.
from wsgiref.validate import validator


nota = int(input("Qual sua nota?"))
match nota:
    case 0:
        print("Você está reprovado, faltam 5 pontos para a aprovação")
    case 1:
        print("Você está reprovado, faltam 4 pontos para a aprovação")
    case 2:
        print("Você está reprovado, faltam 3 pontos para a aprovação")
    case 3:
        print("Você está reprovado, faltam 2 pontos para a aprovação")
    case 4:
        print("Você está reprovado, falta 1 ponto para a aprovação")
    case 5:
        print("Você está aprovado na média")
    case 6:
        print("Você está aprovado, por um ponto")
    case 7:
        print("Você está aprovado, por dois pontos")
    case 8:
        print("Você está aprovado, por três pontos")
    case 9:
        print("Você está aprovado, por quatro pontos")
    case 10:
        print("Você está aprovado, com nota máxima!")

#exemplo 2:
nota = int(input("qual sua nota? "))
match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("reprovado")
    case 5 | 6 | 7 | 8 | 9 | 10:
        print("aprovado")

#exemplo 3:

notas_finais_classe = [10, 8, 2, 1, 0]
for n in notas_finais_classe:
    match n:
        case 0 | 1 | 2 | 3 | 4:
            print("Aluno(a) reprovado(a): " + str(n))
        case 5 | 6 | 7 | 8 | 9 | 10:
            print("Aluno(a) aprovado(a)" + str(n))

#aplicar desconto:

def veredito(nota):
    match nota:
        case 0 | 1 | 2 | 3 | 4 :
            print(f"Aluno(a) reprovado(a): {nota}")
        case 5 | 6 | 7 | 8 | 9 | 10:
            print(f"Aluno(a) aprovado(a): {nota}")

if __name__ == '__main__':
    notas = [10, 8, 9, 1, 0]
    for n in notas:
        veredito(n)

def aplicarDesconto(valor, percentual):
        valor = valor - (valor * (percentual / 100))
        return validator

if __name__ == '__main__':
    print(aplicarDesconto(100, 20))

#exemplo 2:

def aplicarDesconto(valor, percentual):
    fator = percentual / 100
    valor_a_descontar = valor * fator 
    valor_final = valor - valor_a_descontar
    return valor_final

#valor = valor - (valor * (percentual / 100))
#return valor

#alterar a função veredito

def veredito(nota):
    if nota < 5:
        print(f"Aluno Reprovado: {nota}")
    else:
        print(f"Aluno Aprovado: {nota}")

if __name__ == '__main__':
    notas = [10, 4.5, 9, 1, 0]
    for n in notas:
        veredito(n)


