###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Gráfico de Recorrência
# Nome:
# RA:
###################################################

# Leitura de dados
lista_valores = []

N = int(input())
dic_recorrencia = {}
for i in range(N):
    lista_valores.append(int(input()))
    
L = int(input()) #Limiar
for valores in lista_valores:
    for i in range(0,N):
        valor_absoluto = (lista_valores[i]  - valores)
        if valor_absoluto < 0:
            valor_absoluto *= -1
        if i < (len(lista_valores)-1):
            if valor_absoluto > L:
                print("1", end=" ")
            else:
                print("0", end=" ")
        else:
            if valor_absoluto > L:
                print("1")
            else:
                print("0")
                
        
        
           




# Impressão do gráfico de recorrência