###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Picos e Vales I
# Nome:
# RA:
###################################################

# leitura e verificação dos picos e vales
i = int(input("Digite o valor para a sua colina ou vale: "))
lista = []
lista.append(i)

vales = 0
picos = 0

while i != 0:
    i = int(input("Digite o próximo valor: "))
    lista.append(i)
for x in range (len(lista) - 2):
    if lista[x-1] > lista[x] and lista[x+1] > lista[x]:
        vales += 1
    if lista[x-1] < lista[x] and lista[x+1] < lista[x]:
        picos += 1

# impressão da saída
print("Quantidade de picos:", picos)
print("Quantidade de vales:", vales)
