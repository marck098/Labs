###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

def difença(numero):
    numero_str = str(numero)
    crescente  = int(''.join(sorted(numero_str)))
    decrescente  = int(''.join(sorted(numero_str,reverse = True)))
    difença_analisada = decrescente - crescente 
    return difença_analisada

def mais_amigos(numero, qtd_interacoes):
    numero_analisado = difença(numero)
    qtd_interacoes += 1
    if numero_analisado == 495:
        return qtd_interacoes
    else:
        return mais_amigos(numero_analisado, qtd_interacoes)

def bubbleSort(lista_it, lista_num):
    n = len(lista_it)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lista_it[j] > lista_it[j + 1]:
                lista_it[j], lista_it[j + 1] = lista_it[j+1], lista_it[j]
                lista_num[j], lista_num[j + 1] = lista_num[j+1], lista_num[j]
            elif lista_it[j] == lista_it[j + 1] and lista_num[j] > lista_num[j + 1]:
                lista_it[j], lista_it[j + 1] = lista_it[j+1], lista_it[j]
                lista_num[j], lista_num[j + 1] = lista_num[j+1], lista_num[j]
                
# Leitura da sequência
numeros = [int(i) for i in input().split()]

# Ordenação dos amigos do 495                
lista_qtdIteracoes = []
for numero in numeros:
    aux = mais_amigos(numero, 0)
    lista_qtdIteracoes.append(aux)    
bubbleSort(lista_qtdIteracoes, numeros)

# Impressão da resposta
print(*numeros)