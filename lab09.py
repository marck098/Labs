###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Criptografia Cíclica
# Nome:Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

# Leitura da entrada
p = input()
codigo = list(input())
ja_trocou = []
for i in codigo:
    ja_trocou.append(0)

# Decodificação da mensagem
for index_p,letra_p in enumerate(p):
        for index_codigo, letra_palavra in enumerate(codigo):
            if letra_p == letra_palavra.lower():
                if ja_trocou[index_codigo] == 0:
                    if letra_palavra.isupper() == True:
                        codigo[index_codigo] = p[(index_p -1)].upper()
                        ja_trocou[index_codigo] = 1
                    else:
                        codigo[index_codigo] = p[(index_p -1)]
                        ja_trocou[index_codigo] = 1


# Impressão da saída
print("".join(codigo))