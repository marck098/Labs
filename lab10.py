#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
#####################################################

# Leitura do mapa
n, m = [int(i) for i in input().split()]
mapa = []
for _ in range(n):
  linha = [int(i) for i in input().split()]
  mapa.append(linha)
  
# Leitura e processamento dos movimentos dos jogadores
q = int(input())
resultados = []

def avalia_tesouro(tesouro_inventario,linha, coluna, mapa):
    tesouro_local = mapa[linha][coluna]
    if tesouro_local >= tesouro_inventario:
        aux_troca = tesouro_inventario
        tesouro_inventario = tesouro_local
        mapa[linha][coluna] = aux_troca
    return tesouro_inventario

for n in range(1,q+1):
    l_inicial, c_inicial = [int(i) for i in input().split()]
    movimentos = input()
    tesouro_inventario = 0
    for coordenada in movimentos:
        tesouro_inventario = avalia_tesouro(tesouro_inventario, l_inicial,c_inicial,mapa)
        if coordenada == 'N':
            l_inicial -= 1
        elif coordenada == 'S':
            l_inicial += 1
        elif coordenada == 'O':
            c_inicial -= 1
        elif coordenada == 'L':
            c_inicial += 1
        tesouro_inventario = avalia_tesouro(tesouro_inventario, l_inicial,c_inicial,mapa)
    resultados.append("Caçador {}: {}".format(n,tesouro_inventario))
    
# Impressão da saída
for item in resultados:
    print(item) 