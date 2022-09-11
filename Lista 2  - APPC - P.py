#EX 1:

def triangulo(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if (a < b + c) and (c < a + b) and (b < a + c):
            return True
        else:
            return False
    else:
        return False
def verificar_tipo(a, b, c):
    if a == b and c == a:
        print('Triângulo Equilátero')
    elif a != b and b != c and a != c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
        
if __name__ == '__main__':
    while True:
        try :
            a = int(input('Lado A:\n'))
            b = int(input('Lado B:\n'))
            c = int(input('Lado C:\n'))
            break
        except:
            print('Dados errados, tente novamente!')
    if triangulo(a, b, c):
        verificar_tipo(a, b, c)

#EX 2:

numero_linhas = int(input('Digite um número de linhas maior ou igual a 2: '))
contador = 1
for r in range(1, numero_linhas + 1):
    for i in range(1, r + 1):
        print(f'{contador:<6}',end = '')
        contador += 1
    print()

#EX 3:

def formatacao_cpf(cpf):
    if len(cpf) < 11:
        cpf = cpf.zfill(11)
    cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return cpf_formatado
 
def formatacao_cep(cep):
    if len(cep) < 8:
        cep = cep.zfill(8)
    cep_formatado = '{}-{}'.format(cep[:5], cep[5:])
    return cep_formatado

def formatacao_end(rua, numero, bairro, cidade, cep, pais):
    end_formatado = (f'{rua}, nº {numero}, {bairro}, {cidade}, {cep}, {pais}')
    return end_formatado

def formatacao_data(cidade, dia, mes, ano):
    data_formatada =(f'{cidade}, {dia} do mês {mes} de {ano}')
    return data_formatada

def formatacao_final(nome, cpf, endereco, data):
    format_final =(f'Eu, {nome}, portador do CPF: {cpf} declaro que resido neste endereço: {endereco}.\n Por ser verdade, firmo a presente declaração.\n {data}')
    return format_final


if __name__ == '__main__':
    nome = input('Digite o nome: ')
    cpf = input('Digite o cpf: ')
    cep = input('Digite o cep: ')
    rua = input('Digite o nome da rua: ')
    numero = input('Digite o numero da casa: ')
    bairro = input('Digite o bairro: ')
    cidade = input('Digite a cidade: ')
    pais = input('Digite o país: ')
    dia = input('Digite o dia de hoje: ')
    mes = input('Digite o mês de hoje: ')
    ano = input('Digite o ano de hoje: ')

    print(formatacao_final(nome, formatacao_cpf(cpf), formatacao_end(rua, numero, bairro, cidade, formatacao_cep(cep), pais), formatacao_data(cidade, dia, mes, ano)))

#EX 4:


#EX 5:

def torreHanoi(n , a, b, c):
    if n == 1:
        print("mover disco de", a, "para haste", b)
        return 
    torreHanoi(n - 1, a, c, b)
    print("mover disco", n,"de", a, "para haste", b)
    torreHanoi(n - 1, c, b, a)
          
torreHanoi(3, 'a', 'b', 'c')

#EX 6:

from cmath import isinf

lista = [[1, 2, 3], 4, 5, 6]
contador = 0
for sub_lista in lista:
    if isinstance(sub_lista, list):
        contador += 1
print(f'O numero de sublistas é: ', contador)

#EX 7:

from re import T


def tripla_pitagorica(numero_1,numero_2,numero_3):
    numeros=[numero_1,numero_2,numero_3]
    numeros.sort()
    teste=[]
    for n in numeros:
        teste.append(n**2)
    if teste[0] + teste[1] == teste[2]:
        return True

if __name__=="__main__":
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    numero_3 = int(input('Digite o terceiro número: '))
    if tripla_pitagorica(numero_1,numero_2,numero_3):
        print("É possivel")
    else:
        print("Não é possivel")

#EX 8:

def soma_divisiveis(numero_inicial, numero_final, divisor):
    contador = 1
    acumulador = 0
    while numero_inicial <= numero_final:
        if contador % divisor == 0:
            acumulador += contador
        numero_inicial += 1
        contador += 1
    return acumulador
print(soma_divisiveis(1,10,2))

#EX 9:

def Mediana(lista_numeros):
    if (len(lista_numeros) + 1) % 2:
        teste = (lista_numeros[(len(lista_numeros) // 2) -1] + lista_numeros[(len(lista_numeros)) // 2]) /2
        print(teste)
    else:
        print(lista_numeros[len(lista_numeros) / 2])

lista = []
contador = 0
while(True):
    l = float(input("Digite a lista numérica: "))
    lista.append(l)
    continuar = input("Deseja continuar? ")
    if(continuar in "nao NAO n NÃO não"):
        break
     
Mediana(lista)

#EX 10:

computadores = {}
COD_computador = 0
contador = 0
lista_computador = []
while(True):
    COD_computador += 1
    preco_custo = float(input('Digite o preço de custo: '))
    preco_venda = float(input('Digite o preço de venda: '))
    qtd_estoque = float(input('Digite a quantidade em estoque: '))
    lista_computador = [preco_custo, preco_venda, qtd_estoque]
    computadores[COD_computador] = lista_computador
    contador += 1
    continuar = input("Deseja continuar?")
    if continuar in "NÃOnão":
        break
for c, j in computadores.items():
    print(f"COD: {c}")
    if isinstance(j,list):
        for i in j:
            print(i)
        total = (j[1] - j[0]) * j[2]
        print(round(total))
    else:
        print(j)