import numpy as np
from egcd import egcd

alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

letraPraIndex = dict(zip(alfabeto, range(len(alfabeto))))
indexPraLetra = dict(zip(range(len(alfabeto)), alfabeto))

def matrizInversa(matriz, modulo):

    determinante = int(np.round(np.linalg.det(matriz)))
    determinanteInversa = egcd(determinante, modulo)[1] % modulo
    matrizInversa = (determinanteInversa * np.round(determinante * np.linalg.inv(matriz)).astype(int) % modulo)

    return matrizInversa

def criptografia(mensagem, K):
    criptografia = ""
    mensagemNumero = []

    for letra in mensagem:
        mensagemNumero.append(letraPraIndex[letra])

    separarP = [mensagemNumero[i : i + int(K.shape[0])]
        for i in range(0, len(mensagemNumero), int(K.shape[0]))]

    for P in separarP:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letraPraIndex[" "])[:, np.newaxis]

        numeros = np.dot(K, P) % len(alfabeto)
        n = numeros.shape[0]

        for index in range(n):
            numero = int(numeros[index, 0])
            criptografia += indexPraLetra[numero]

    return criptografia


def descriptografia(cifra, K_inversa):
    descriptografia = ""
    cifraNumero = []

    for letra in cifra:
        cifraNumero.append(letraPraIndex[letra])

    separarC = [cifraNumero[i : i + int(K_inversa.shape[0])]
        for i in range(0, len(cifraNumero), int(K_inversa.shape[0]))]

    for C in separarC:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numeros = np.dot(K_inversa, C) % len(alfabeto)
        n = numeros.shape[0]

        for idx in range(n):
            numero = int(numeros[idx, 0])
            descriptografia += indexPraLetra[numero]

    return descriptografia

def main():
    nome = input('Insira a senha: ')
    if len(nome) % 2 != 0:
        mensagem = nome.lower()
        letra = mensagem[len(mensagem) - 1]
        mensagem = mensagem + letra
    else:
        mensagem = nome.lower()

    K = np.matrix([[3, 3], [2, 5]])
    K_inversa = matrizInversa(K, len(alfabeto))

    mensagemCriptografada = criptografia(mensagem, K)
    mensagemDescriptografada = descriptografia(mensagemCriptografada, K_inversa)

    print("Mensagem Original: " + mensagem)
    print("Mensagem Criptografada: " + mensagemCriptografada)
    print("Mensagem Descriptografada: " + mensagemDescriptografada)

main()