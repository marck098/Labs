###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Anagramas
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

# Leitura das palavras
lista_palavras = []
anagramas = {}

n = int(input())
for i in range(n):
    lista_palavras.append(input())

# Agrupamento dos anagramas    
for i in lista_palavras:
    c1 = "".join(sorted(i))
    if c1 not in anagramas.keys():
        anagramas[c1] = []
    for j in lista_palavras:
        c2 = "".join(sorted(j))
        if c1 == c2 and j not in anagramas.get(c1):
            anagramas[c1].append(j)
            
# Impressão da saída
for i in anagramas.values():
    print("-".join(i))