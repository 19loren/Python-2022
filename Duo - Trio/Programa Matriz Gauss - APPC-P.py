#Loren Tavolaro 21012402
#Luiza Limoli 22016388


def permuta(linha, perm, perms):
    if not linha:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin] + linha[lin + 1:len(linha)], perm + [linha[lin]], perms)

def permutacoes(linha):
    perms = []
    permuta(linha, [], perms)
    return perms


def listaOrdenadaGenerica(m):
    lista_linhas = []
    for pos in range(len(m)):
        lista_linhas.append(pos)
    return lista_linhas


def combinacoesDeLinhas2a2(m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin + 1, len(m)):
            ret.append([lin, col])
    return ret


def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a / b


def divDumVetorPorOutro(x, y):
    ret = []
    for i in range(len(x) - 1):
        ret.append(divisao(x[i], y[i]))
    return ret


def coeficientesPossiveis(comb, m):
    vet = []
    for pos in range(len(comb)):
        vet.append(divDumVetorPorOutro(m[comb[pos][0]], m[comb[pos][1]]))
    if tudoIgual(vet):
        return False
    else:
        return True


def tudoIgual(vet):
    for pos in range(len(vet)):
        vetComp = vet[pos]
        if all(i == vetComp[0] for i in vetComp):
            return True
        return False


def haZeroNaDiagonal(m, permL, permC):
    for pos in range(len(m)):
        if m[permL[pos]][permC[pos]] == 0:
            return True
    return False


def poeUmNaDiagonalPrincipalNaLinha(lin, m, permL, permC):
    divisor = m[permL[lin]][permC[lin]]
    for col in range(len(m)):
        m[permL[lin]][permL[col]] = divisao(m[permL[lin]][permL[col]], divisor)
    m[permL[lin]][len(m)] = divisao(m[permL[lin]][len(m)], divisor)


def poeZeroNaColuna(m, col, permL, permC):
    vetorMult = []

    for pos in range(len(m) + 1):
        vetorMult.append(m[permL[col]][pos])

    vetorMult.append(m[permL[col]][len(m)])

    for lin in range(0, len(m)):
        mult = m[permL[lin]][permC[col]]
        if lin != col:
            for rec in range(len(m) + 1):
                m[permL[lin]][rec] = m[permL[lin]][rec] - (mult * vetorMult[rec])



def temZeroNaColuna(m, col):
    for lin in range(len(m) - 1):
        if m[lin][col] == 0:
            return True
    return False


def quantosZerosTem(m, permL, permC):
    while haZeroNaDiagonal(m, permL, permC):
        count = 0
        while count < len(m):
            if m[count][count] == 0:
                return count

            count += 1


def comoSeLivrarDeZerosNaDiagonal(matriz):
    perms = permutacoes(list(range(len(matriz))))
    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(matriz, perms[i], perms[j]):
                return [perms[i], perms[j]]

    return None


def haAlgoAlemDeZeroNaColuna(matriz, col, permL, permC):
    for i in range(len(matriz)):
        if matriz[permL[i]][permC[col]] != 0:
            return True
    return False


def ondeTemZero(m):
    for lin in range(len(m) - 1):
        if m[lin][lin] == 0:
            return lin


def carregaMatriz(nomeArq):
    arq = open(nomeArq, "r")
    qtdLins = int(arq.readline())

    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()

        linha = []
        for col in range(qtdLins + 1):
            linha.append(float(texto[col]))

        ret.append(linha)

    arq.close()
    return ret


def __main__():

    try:
        matriz = [[0, 3, 2, 28],
                  [4, 0, 2, 24],
                  [2, 3, 0, 16]]
        perm = listaOrdenadaGenerica(matriz)
        permL = perm
        permC = perm

        print(matriz)
        comb = combinacoesDeLinhas2a2(matriz)
        res = []
        for pos in range(len(matriz)):
            res.append(divDumVetorPorOutro(matriz[comb[pos][0]], matriz[comb[pos][1]]))

        if tudoIgual(res):
            print("A divisão dos coeficientes de duas ou mais linhas é idêntica! A matriz não é solucionável!")

        if haZeroNaDiagonal(matriz, permL, permC):
            vetorPerms = comoSeLivrarDeZerosNaDiagonal(matriz)
            permL = vetorPerms[0]
            permC = vetorPerms[1]

        for pos in range(len(matriz)):
            poeUmNaDiagonalPrincipalNaLinha(pos, matriz, permL, permC)

            if haAlgoAlemDeZeroNaColuna(matriz, pos, permL, permC):
                poeZeroNaColuna(matriz, pos, permL, permC)


        print(matriz)

    except TypeError:
        print("Não é possível resolver essa matriz!")


__main__()
