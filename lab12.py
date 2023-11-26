###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Mansão Mal Assombrada I
# Nome: 
# RA: 
###################################################

# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()

# Leitura das posições de cada fantasma e de cada caçador



# Simulação do movimento dos fantasmas



# Impressão da saída