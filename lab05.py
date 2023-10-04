###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - A Última Rodada
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

# Leitura da primeira linha
N, V, P = input().split()
N = int(N) #partes da roleta
V = float(V) #valor que seu amigo precisa para a viagem
P = float(P) #valor do prêmio que ele acumulou até essa rodada
i = 0
P2 = 0
lista_valoresP = []
# Leitura da roleta
while  i < N:
    aux = input().split()
    if aux[2] == "%": #Condicional para +- %
        if aux[0] == "-":
            aux_percent = int(aux[1])
            P2 = P - (P * (aux_percent/100))
            if P2 < 0.0:
                P2 = 0.0
        elif aux[0] == "+":
            aux_percent = int(aux[1])
            P2 = P + (P * (aux_percent/100))
            if P2 < 0.0:
                P2 = 0.0
    elif aux[2] == "Reais": #Condicional para +- R$
        if aux[0] == "-":
            valor_int = int(aux[1])
            P2 = P - valor_int
            if P2 < 0.0:
                P2 = 0.0
        elif aux[0] == "+":
            valor_int = int(aux[1])
            P2 = P + valor_int
            if P2 < 0.0:
                P2 = 0.0
    lista_valoresP.append(P2)
    i += 1 
 
# Calculo da probabilidade    
somaValores = 0
possibilidade_ganhar = 0

for i in lista_valoresP:
    somaValores += i  
    if i >= V:
        possibilidade_ganhar += 1 
prob_viagem = (possibilidade_ganhar/N)*100
    
premio_medio = somaValores/N
# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(prob_viagem))
# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(premio_medio))