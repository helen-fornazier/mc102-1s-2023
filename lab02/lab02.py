###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Trem das Onze
# Nome:
# RA:
###################################################

# Leitura de dados

x1 = int()
if x1 >= 24:
    x1 = 0
y1 = int()
if y1 >= 60:
    y1 = 0
w1 = int()
z1 = int()
yf1 = float(y1/100)
ddv1 = float (w1/z1)
horario1 = float(x1+yf1)

x2 = int()
if x2 >= 24:
    x2 = 0
y2 = int()
if y2 >= 60:
    y2 = 0
w2 = int()
z2 = int(input()
yf2 = float(y2/100)
ddv2 = float (w2/z2)
horario2 = float(x2+yf2)

chegou = True
nao = False

# Cálculo do tempo gasto para chegar a parada do trem

if (x1 == 23):      
    print(nao)

elif (x2 == 23):   
    print(nao)

else:
    horario1 += ddv1

# Impressão da resposta

if horario1 >= 23:
    print(nao)
        
else:
    horario2 += ddv2

if horario2 >= 23:
    print(nao)

elif horario2 <= horario1:
    print(nao)
        
else:
    print(chegou)
