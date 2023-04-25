###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Escolha da Missão
# Nome:
# RA:
###################################################

# leitura de dados

nivel = int(input())
ataque = int(input())
defesa = int(input())
gold = int(input())
missao = int()


# Escolha da missão

if ((nivel >= 5) and (ataque >= 40) and (defesa >= 50) and (gold >= 50)):
    gold -= 50
    missao = 5
    gold += 130

elif ((nivel >= 5) and (defesa >= 50) and (ataque >= 50)):
        missao = 6
        gold+=60

elif ((nivel >= 3) and (ataque < defesa) and (gold >= 50)):
    gold -= 50
    missao = 3
    gold += 100

elif ((nivel >= 3) and (ataque >= 20) and (defesa >= 30)):
    gold += 40
    missao = 4

elif ((nivel >= 5) and (defesa >= 50)):
    gold += 30
    missao = 6
    print("Missão escolhida: ")
    print("Moedas de ouro: ", gold)
    
elif ((ataque >= 30) and (defesa >= 10)):
    gold += 25
    missao = 1
    print("Missão escolhida: ", missao)
    print("Moedas de ouro: ", gold)

elif ((nivel >= 3) and (gold >= 20)):
    gold -= 20
    missao = 4

elif ((defesa >= 30) and (gold >= 30)):
    gold -= 30
    missao = 2
    gold += 40

# Impressão da missão escolhida
print('missão escolhida:', missao)
print('moedas de ouro:', ouro)
