#SEGUNDA ATIVIDADE 2

#Loren Severi Tavolaro 21012402
#Luiza Eduarda Limoli 22016388
#Luis Felipe Federicci 22013911

import os

lista_moedas = []

def popular():

    pais_de_origem = str(input("País de origem: "))
    moeda = str(input('Moeda: '))

    try:
        ano = int(input('Ano: '))
        valor_face = float(input('Valor da face da moeda: '))
        valor_mercado = float(input('Valor de mercado: '))
    except ValueError:

        print('Valor incorreto, utilize um número.')
    
    dic = {
        'pais_de_origem': pais_de_origem,
        'ano': ano,
        'moeda': moeda,
        'valor_face': valor_face,
        'valor_mercado': valor_mercado
    }

    lista_moedas.append(dic)

def cabecalho():
    print('-' * 45)
    print('PONTIFÍCIA UNIVERSIDADE CATÓLICA DE CAMPINAS')
    print('\tCurso de Engenharia de Software')
    print('-' * 45)
    print('BEM VINDO(A) AO PROGRAMA DE MOEDAS')
    print('-' * 45)
    return

def imprime(moedas):

    print ("{:<16} {:<5} {:<10} {:<15} {:<15}".format('País de origem','Ano','Moeda', 'Valor da face', 'Valor de mercado'))
    for moeda in moedas:
        print ("{:<16} {:<5} {:<10} {:<15} {:<15}".format(moeda['pais_de_origem'], moeda['ano'], moeda['moeda'], moeda['valor_face'], moeda['valor_mercado']))

def consultarDadosMoeda():
    moedaSolicitada = str(input('Digite a moeda: '))
    for moeda in lista_moedas:
        if moeda['moeda'] == moedaSolicitada:
            moedaEncontrada = moeda
    try:
        imprime([moedaEncontrada])
    except Exception:
        os.system('cls')
        print('Moeda não encontrada.')

def consultarMoedasValorVenda():
    try:
        valorSolicitado = float(input('Digite o valor de venda das moedas: '))
    except ValueError:
        os.system('cls')
        print('Digite um valor de venda válido.')
        return

    moedasEncontradas = []

    for moeda in lista_moedas:
        if moeda['valor_mercado'] == valorSolicitado:
            moedasEncontradas.append(moeda)
    if len(moedasEncontradas) == 0:
        os.system('cls')
        print('Nenhuma moeda encontrada com esse valor de venda.')
        return

    imprime(moedasEncontradas)
    
def menu():
    #os.system('cls')
    print()
    print('<<< OPERAÇÕES >>>')
    print()
    print('''1. Consultar DADOS de Uma Moeda
2. Incluir Uma Nova Moeda;
3. Imprimir TODAS as moedas com um determinado Valor de Venda
4. Imprimir TODAS as Moedas no formato de Tabela
0. Encerrar Programa''')
    
    try:
        escolha = int(input('Escolha <0 a 4>: '))
    except ValueError:
        os.system('cls') 
        print('Valor incorreto, utilize um número.')
        return menu()

    os.system('cls') 
    if not (escolha >= 0 and escolha <= 4):
        print('Valor incorreto, escolha uma opção entre 0 e 4.')
        return menu()
    
    if escolha == 1:
        consultarDadosMoeda()
    
    elif escolha == 2:
        popular()

    elif escolha == 3:
        consultarMoedasValorVenda()
      
    elif escolha == 4:
        imprime(lista_moedas)
        
    elif escolha == 0:
        fecharPrograma()


def fecharPrograma():
    print('-' * 45)
    print('OBRIGADA POR USAR ESSE PROGRAMA')
    print('-' * 45)
    exit()


if __name__ == '__main__':
    cabecalho()
    while True:
        menu()
