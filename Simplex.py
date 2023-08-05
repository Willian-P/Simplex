import numpy as np
import math


def Multiplicacao_matrizes(matrizA: list, matrizB: list) -> float:
    matrizC = np.matmul(matrizA, matrizB)
    return matrizC


def Multiplicacao_vetores(vetorA: list, vetorB:list) -> float:
    res = np.dot(vetorA, vetorB)
    return res


def trocar_colunas(B, N, coluna_B, coluna_N):
    aux = np.copy(N[:, coluna_N])
    N[:, coluna_N] = B[:, coluna_B]
    B[:, coluna_B] = aux


B = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])

N = np.array([[1, 0],
              [0, 0],
              [0, 1]])


qtd_colunas = B.shape[1] + N.shape[1]
print('qtd_Colunas: ', qtd_colunas)

# Trocando colunas entre as matrizes básicas e não básicas
if np.linalg.det(B) == 0:
    for coluna_B in range(B.shape[1]):
        for coluna_N in range(N.shape[1]):
            trocar_colunas(B, N, coluna_B, coluna_N)
            print(f'B{coluna_B} com N{coluna_N}')
            print(B)
            print(N)
            print('\n')

            if np.linalg.det(B) != 0:
                break

A = B
print('A = \n', A)

n = A.shape[0]
print('n = ', n)

I = np.identity(n)

if np.linalg.det(A) != 0:
    AID = np.hstack((A, I))

    for i in range(n):
        pivo = AID[i][i]

        if pivo == 0:
            for j in range(i + 1, n):
                if AID[j, i] != 0:
                    AID[[i, j]] = AID[[j, i]]
                    break
                else:
                    print('Matriz não possui inversa')
                    break

            pivo = AID[i, i]

        AID[i] /= pivo

        for j in range(n):
            if j != i:
                multiplicador = AID[j, i]
                AID[j] -= multiplicador * AID[i]

    inversa = AID[:, n:]

    print(f'Inversa:\n{inversa}')
else:
    print('Matriz não possui inversa')


# Cálculo da solução básica
b = [4, 3, 7/2]

x_chapeu_B = np.zeros((n))
for j in range(n):
    for i in range(n):
        x_chapeu_B[i] += inversa[i][j] * b[j]
print(f'x_chapeu_B: {x_chapeu_B}')

x_chapeu_N = np.zeros(N.shape[1])
print(f'x_chapeu_N: {x_chapeu_N}')

cB = [-2, -1, 0]
cN = [0, 0]

# CÁLCULO CUSTOS RELATIVOS

# Vetor multiplicador simplex
lambda_T = Multiplicacao_matrizes(cB, inversa)
print(f'lambda_T: {lambda_T}')

# Custos relativos
c_chapeu_n = np.zeros(N.shape[1])
for i in range(N.shape[1]):
    for j in range(N.shape[0]):
        c_chapeu_n[i] += lambda_T[j] * N[j][i]

print(f'c_chapeu_n: {c_chapeu_n}')

qualquerNomeSoPraFazerUmTeste = np.zeros(N.shape[1])

kMenor = -1
menor = np.Infinity

for i in range(qualquerNomeSoPraFazerUmTeste.shape[0]):
    qualquerNomeSoPraFazerUmTeste[i] = x_chapeu_N[i] - c_chapeu_n[i]
    print(qualquerNomeSoPraFazerUmTeste[i])
    if qualquerNomeSoPraFazerUmTeste[i] < menor:
        menor = qualquerNomeSoPraFazerUmTeste[i]
        kMenor = i


print(qualquerNomeSoPraFazerUmTeste[kMenor])

aux = -1

for i in range(qualquerNomeSoPraFazerUmTeste.shape[0]):
    if x_chapeu_B[i] / qualquerNomeSoPraFazerUmTeste[i] >= 0 and x_chapeu_B[i] / qualquerNomeSoPraFazerUmTeste[i] < aux and qualquerNomeSoPraFazerUmTeste[i] != 0:
        aux = i

print(qualquerNomeSoPraFazerUmTeste[aux])