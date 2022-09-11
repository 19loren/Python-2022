#PROVA SUBSTITUTIVA
#Loren Severi Tavolaro 21012402

import os

lista_filmes = []

def filmes():

    titulo_filme = str(input('Título: '))
    diretor = str(input('Diretor: '))
    try:
        codigo_filme = int(input('Código do filme: '))
        ano_lancamento = int(input('Ano de Lançamento: '))
        classificacao = int(input('Classificação (1-5): '))
    except ValueError:

        print('Valor incorreto, utilize um número.')
    
    dic = {
        'codigo_filme': codigo_filme,
        'ano_lancamento': ano_lancamento,
        'titulo_filme': titulo_filme,
        'diretor': diretor,
        'classificacao': classificacao 
    }

    lista_filmes.append(dic)

def imprime(filmes):
    print('\tImpressão de Todos os Filmes')
    print('='*45)

    for filme in filmes:
        print('Código: ',filme['codigo_filme'],'\nTítulo: ',filme['titulo_filme'],'\nDiretor: ',filme['diretor'],'\nAno: ',filme['ano_lancamento'],'\nClassificação: ',filme['classificacao'])
        print('='*45)

def consultarDadosFilme():
    codigoSolicitado = int(input('Digite o código do filme: '))
    for codigo in lista_filmes:
        if codigo['codigo_filme'] == codigoSolicitado:
            codigoEncontrado = codigo
    try:
        os.system('cls')
        imprime([codigoEncontrado])
    except Exception:
        os.system('cls')
        print('Não existem filmes com esse código.')

def consultarFilmesDiretor():
    try:
        diretor = str(input('Diretor a ser procurado: '))
    except NameError:
        os.system('cls')
        print('Digite um diretor válido.')
        return

    filmesEncontrados = []

    for filme in lista_filmes:
        if filme['diretor'] == diretor:
            filmesEncontrados.append(filme)
    if len(filmesEncontrados) == 0:
        os.system('cls')
        print('Não foi encontrado nenhum filme produzido pelo diretor inserido.')
        return

    imprime(filmesEncontrados)

def consultarClassFilme():
    print('='*45)
    try:
        classFilme = int(input('Classificação a ser procurada (1-5): '))
    except (classFilme >= 0 and classFilme <= 5):
        os.system('cls')
        print('Digite um valor entre 1 e 5.')
        return

    filmesEncontrados = []

    for filme in lista_filmes:
        if filme['classificacao'] == classFilme:
            filmesEncontrados.append(filme)
    if len(filmesEncontrados) == 0:
        os.system('cls')
        print('Não foi encontrado nenhum filme com a classificação inserida.')
        return

    imprime(filmesEncontrados)
    
def menu():
    #os.system('cls')
    print()
    print('<<< OPERAÇÕES >>>')
    print()
    print('''1. Consultar DADOS de um filme
2. Incluir novos filmes
3. Imprimir todos os filmes de determinado diretor
4. Imprimir todos os filmes com determinada classificação
5. Imprimir todos os filmes
0. Encerrar Programa''')
    
    try:
        escolha = int(input('Escolha <0 a 5>: '))
    except ValueError:
        os.system('cls') 
        print('Valor incorreto, utilize um número.')
        return menu()

    os.system('cls') 
    if not (escolha >= 0 and escolha <= 5):
        print('Valor incorreto, escolha uma opção entre 0 e 5.')
        return menu()
    
    if escolha == 1:
        consultarDadosFilme()
    
    elif escolha == 2:
        filmes()

    elif escolha == 3:
        consultarFilmesDiretor()
      
    elif escolha == 4:
        consultarClassFilme()
        
    elif escolha == 5:
        imprime(lista_filmes)

    elif escolha == 0:
        fecharPrograma()


def fecharPrograma():
    print('-' * 45)
    print('OBRIGADA POR USAR ESSE PROGRAMA')
    print('-' * 45)
    exit()


if __name__ == '__main__':
    while True:
        menu()
