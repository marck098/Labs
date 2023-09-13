###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha Pokémon
# Nome: Marcos Vinicius de Carvalho Araujo
# RA: 242711
###################################################

# Leitura do hp e velocidade dos pokémons
hp_Ivysaur = float(input())
hp_Pikachu= float(input())
vel_Ivysaur = float(input())
vel_Pikachu = float(input())
# Leitura dos ataques dos turnos
while hp_Ivysaur > 0 and hp_Pikachu > 0:
    if vel_Ivysaur > vel_Pikachu:
        x = float(input())
        y = float(input())
        x = x*y
        if hp_Pikachu - x < 0:
            hp_Pikachu = 0
        else:
            hp_Pikachu -= x
        x = float(input())
        y = float(input())
        x = x*y
        if hp_Ivysaur - x < 0:
            if hp_Pikachu > 0:
                hp_Ivysaur = 0
        else:
            if hp_Pikachu > 0:
                hp_Ivysaur -= x
    else:
        x = float(input())
        y = float(input())
        x = x*y
        if hp_Ivysaur - x <0:
            hp_Ivysaur = 0
        else:
            hp_Ivysaur -= x
        x = float(input())
        y = float(input())
        x = x*y
        if hp_Pikachu - x < 0:
            if hp_Ivysaur > 0:
             hp_Pikachu = 0
        else:
            if hp_Ivysaur > 0:
                hp_Pikachu -= x
    print("HP Ivysaur =", int(hp_Ivysaur))
    
    print("HP Pikachu =", int(hp_Pikachu))
        
# Impressão do vencedor
if hp_Ivysaur > hp_Pikachu:
    print("Pokémon Vencedor: Ivysaur")
    
    print("HP do Vencedor:", int(hp_Ivysaur))
else:
    print("Pokémon Vencedor: Pikachu")
    
    print("HP do Vencedor:", int(hp_Pikachu))