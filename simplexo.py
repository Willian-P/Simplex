import numpy as np
import math

# funcao_objetivo = []
funcao_objetivo = [1, -1, 2]
tipo_funcao = int(input('Digite 0 para função de Maximização ou 1 para função de Minimização: '))

# Inverter função objetivo se for de maximização
if tipo_funcao == 0:
    funcao_objetivo = [-coef for coef in funcao_objetivo]
    print("Função objetivo após inversão:", funcao_objetivo)

num_restricoes = int(input('Informe o número de restrições: '))

matriz = []
B = []
b = []
n = []

for i in range(num_restricoes):
    new = input(f'\nDigite a restrição {i+1} separada por espaços (Exemplo: 1 -2 3 <= 5): ').split()
    linha = []
    
    for j in range(len(new) - 2):  # -2 para excluir o operador de comparação e o valor independente
        linha.append(float(new[j]))
    
    matriz.append(linha)
    operador = new[-2]
    valor_independente = float(new[-1])
    
    if operador == '<=':
        B.append(valor_independente)
    elif operador == '>=':
        B.append(-valor_independente)  # Negativo para transformar em restrição <=
    elif operador == '=':
        B.append(valor_independente)
        n.append(len(funcao_objetivo) + i)  # Índice da variável artificial
    
    b.append(valor_independente)

    n.append(len(funcao_objetivo) + i)  # Índice da variável de folga/artificial

# Preenche z com zeros para as variáveis de folga/artificial
funcao_objetivo += [0] * num_restricoes

print("Matriz de Coeficientes: ", matriz)
print("Vetor B: ", B)
print("Vetor b: ", b)
print("Índices das variáveis não básicas: ", n)
print("Função objetivo: ", funcao_objetivo)