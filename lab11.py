###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

loteamento = []
for j in range(15):
    linha = []
    for i in range(15):
        linha.append("x")
    loteamento.append(linha)

def cria_ruas(ruas_verticas, ruas_horizontais): #cria ruas verticais 
    for indice_c_ruas in ruas_horizontais:
        for item in range(15):
                loteamento[indice_c_ruas][item] = "."
    for linha_lote in range(len(loteamento)):   #cria ruas verticais         
        for indice_v_ruas in ruas_verticais:
            loteamento[linha_lote][indice_v_ruas] = "."

def comprar_lote(oferta_compra):
    # linha 1 coluna 1 linha 2 coluna 2
    area_livre_valor = True
    area_livre_valor = area_livre(oferta_compra)
    if area_livre_valor == True:
        for compra_linha_lote in range(oferta_compra[0], (oferta_compra[2] + 1)):
            for compra_coluna_lote in range(oferta_compra[1], (oferta_compra[3] + 1)):
                    loteamento[compra_linha_lote][compra_coluna_lote] = str(comprador)

def area_livre(oferta_compra):
    for compra_linha_lote in range(oferta_compra[0], (oferta_compra[2] + 1)):
        for compra_coluna_lote in range(oferta_compra[1], (oferta_compra[3] + 1)):
            if loteamento[compra_linha_lote][compra_coluna_lote] == "." or loteamento[compra_linha_lote][compra_coluna_lote]  != "x":
                return False
    return True
        
        
# Leitura de dados
ruas_horizontais = [int(i) for i in input().split()]
ruas_verticais = [int(i) for i in input().split()]

cria_ruas(ruas_verticais, ruas_horizontais)

n = int(input())
for comprador in range(1,n+1):
    oferta_compra = [int(i) for i in input().split()]
    comprar_lote(oferta_compra)
# Processamento



# Impressão da saída
for linha in loteamento:
  print(" ".join(linha))