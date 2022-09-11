##Dicionários - APPC-P

alunos = {'abraao':10, 'beatriz':10, 'bernardo':3.0}
alunos['henrique'] = 7.5
print(alunos)

#dicionário com o exercício anterior de match

def veredito(nome, nota):
    if nota < 5:
        print(f"{nome} - Reprovado(a): {nota}")
    else:
        print(f"{nome} - Aprovado(a): {nota}")

if __name__ == '__main__':
    alunos = {'Adriana':10, 'Alonso':4.3, 'Beatriz':5.0, 'Luiza':1, 'Fernanda':0}
    for nome, nota in alunos.items():
        veredito(nome, nota)


#exercício 2: 
# a) imprima todas as chaves do dicionário  

linguagens = {'C':1986, 'C++':1991, 'Java':1998, 'Python':2000}
for nomes in linguagens:
    print(nomes)

#b) imprima todos os itens do dicionário

linguagens = {'C':1986, 'C++':1991, 'Java':1998, 'Python':2000}
for anos in linguagens.items():
    print(anos)

#outra alternativa

#a) 
for v in linguagens.values():
    print(v)

#b)
for k in linguagens.keys():
    print(k)

#c) adcionar a linguagem haskell no dicionário e o ano de lançamento (2002)
linguagens = {'C':1986, 'C++':1991, 'Java':1998, 'Python':2000}
linguagens['Haskell'] = 2002
print(linguagens)

#d) deletar o haskell
del linguagens['Haskell']
print(linguagens)

#exercício 3:
#faça um programa completo em python que defina um dicionario de alunos, inicialmente vazio, o programa deve pedir a operacao ao usuário
#(ex: digite 1 para inserir o aluno, digite 2 para buscar um anluno pelo nome, digite 3 para buscar um aluno pelo ra, digite 4 para remover um  aluno)
#faca seu programa usando funcoes
#key = RA
#value = nome aluno     fazer input, while, if e um dicionario


def validarOpcaoDigitada(opcao): 
    resultado = False
    if ((opcao>=1) and (opcao<=5)):
        resultado = True
    return resultado

def inserirAluno(dicAlunos, ra, nome_do_aluno):
    dicAlunos[ra] = nome_do_aluno


if __name__ =='__main__':
     alunos = {}
     opcao = int(input("Bem vindo ao programa de alunos. \nMenu: \nDigite a opção:\n 1 - Inserir aluno\n 2 - Procurar aluno por nome \n 3 - Procurar aluno por RA \n 4 - Remover aluno \n 5 - Mostrar todos os alunos\n\nDigite a opção: "))

if (validarOpcaoDigitada(opcao)):
    print("valia.... continua o programa...")
    match opcao:
        case 1: 
            print('Inserir Aluno. Informe os dados:\n')
            ra = input('Insira RA: ')
            nome = input("insira o nome: \n")
            inserirAluno(alunos, ra, nome)

            print("Todos os Alunos", alunos)
        case 2: print("procurar aluno por nome")
        case 3: print("procurar aluno por RA")
        case 4: print("remover aluno por RA")
        case 5: print("Mostrar todos os alunos")
