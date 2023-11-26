###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome:
# RA:
###################################################

# Leitura da sequência
numeros = [int(i) for i in input().split()]
# Ordenação dos amigos do 495

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

# def ordena_amigos(numeros, lista_qtdIteracoes):
#     for index in range(len(numero)):
    

lista_qtdIteracoes = []

for numero in numeros:
    aux = mais_amigos(numero, 0)
    lista_qtdIteracoes.append(aux)
    
print(lista_qtdIteracoes)
    
    
        
    
    
            


# Impressão da resposta

# 1 ordenar os numeros para comparação
    # analisar cada um separadamente
    # organizar de forma crescente e decrescente
   
# 2 criar a recursão
    # analisar quantas iterações o numero realizou até chegar no 495
# 3 comparar iterações entre os numeros