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
ouro = int(input())
missao = int()

# Escolha da missão

if ((nivel >= 5) and (ataque >= 40) and (defesa >= 50) and (ouro >= 50)):
    ouro -= 50
    missao = 5
    ouro += 130

elif ((nivel >= 5) and (defesa >= 50) and (ataque >= 50)):
        missao = 6
        ouro+=60

elif ((nivel >= 3) and (ataque < defesa) and (ouro >= 50)):
    ouro -= 50
    missao = 3
    ouro += 100

elif ((nivel >= 3) and (ataque >= 20) and (defesa >= 30)):
    ouro += 40
    missao = 4

elif ((nivel >= 5) and (defesa >= 50)):
    ouro += 30
    missao = 6
    
elif ((ataque >= 30) and (defesa >= 10)):
    ouro += 25
    missao = 1

elif ((nivel >= 3) and (ouro >= 20)):
    ouro -= 20
    missao = 4

elif ((defesa >= 30) and (ouro >= 30)):
    ouro -= 30
    missao = 2
    ouro += 40

# Impressão da missão escolhida
print('missão escolhida:', missao)
print('moedas de ouro:', ouro)
