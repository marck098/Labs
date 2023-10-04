###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Nota de MC102
# Nome: Marcos Vinicius de Carvalho Araujo 
# RA: 242711
###################################################

# Leitura de dados
lista_notas = []
lista_pesos = []
N = int(input())

for i in range(N):
    lista_notas.append(float(input()))
for i in range(N):
    lista_pesos.append(float(input()))
media = 0.0
denominador = 0.0
numerador = 0.0

# Cálculo da média ponderada dos laboratórios
for i in range(len(lista_pesos)):
    denominador += lista_pesos[i]
    numerador += (lista_pesos[i]*lista_notas[i])
media = numerador/denominador

print("Media laboratorios:", format(media, ".1f").replace(".", ","))

# Verificação da situação do aluno

# Caso o aluno tenha sido reprovado por nota
if media < 2.5:
    nota_final = media
    print("Situacao: Reprovado por nota")
    
# Caso o aluno tenha sido aprovado por nota
elif media >= 5.0:
    nota_final = media
    print("Situacao: Aprovado por nota")
    
# Cálculo da nota do exame, caso o aluno tenha ido para o exame
else:
    denominador_ex  = 0.0
    numerador_ex = 0.0
    media_labs = media
    lista_pesos_exame = []
    lista_notas_exame = []
    
    N_exame = int(input())
    
    for i in range(N_exame):
        lista_pesos_exame.append(float(input()))
    for i in range(N_exame):
        lista_notas_exame.append(float(input()))
        
    for i in range(len(lista_notas_exame)):
        numerador_ex += (lista_pesos_exame[i]*lista_notas_exame[i])
        denominador_ex += lista_pesos_exame[i]
        
    media_exame = numerador_ex/denominador_ex
    
    nota_final = min(5, (media_exame + media_labs)/2)
    # Caso o aluno tenha sido aprovado no exame
    if nota_final == 5:
        print("Situacao: Aprovado no exame")
    # Caso o aluno tenha sido repravado no exame
    else:
        print("Situacao: Reprovado no exame")

# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))
