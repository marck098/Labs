###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Investimento em Renda Fixa
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

# leitura de dados
montante = int(input())
d = int(input())
jurosPoupanca = int(input())
jurosTesouro = int(input())

# cálculo dos rendimentos
poupanca = (montante * (jurosPoupanca/100))
rendimentoTesouro =  montante * (jurosTesouro/100)
	#tributação IR Tesouro Direto:
if d <= 180:
    tributo = rendimentoTesouro * 0.225
elif d > 180 and d <= 360:
    tributo = rendimentoTesouro* 0.2
elif d > 360 and d <= 720:
    tributo = rendimentoTesouro * 0.175
else:
    tributo = rendimentoTesouro * 0.15

tesouro = (rendimentoTesouro - tributo)

# Impressão da saída
print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
	print("Maior rendimento: poupança")
else:
	print("Maior rendimento: tesouro")