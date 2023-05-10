# Primeira lista de exercícios do MC102

# 1. Responda qual tipo de objeto deve ser usado para armazenar cada uma das seguintes
# informações:

# a. A idade de uma pessoa. = int
# b. A área do seu quintal em metros quadrados. = float
# c. A média da quantidade de chuva no mês de fevereiro. = float
# d. O número de estrelas na galáxia. = int

# 2. Considere o trecho de código abaixo:

# 1 a = 10
# 2 b = a
# 3 c = 9
# 4 d = c
# 5 c = c + 1

# Após a execução desse trecho de código, qual será o valor armazenado em cada variável?
#a) 10
#b) 10
#c) ?
#d) ? (= C)

print("Questão 3 = 3, Questão 4 = 4... Questão 10 = 10 (última questão)")
print("0 = Fecha programa")
selector = int(input("Digite a questão desejada: "))

while selector <= 10 and selector >= 3:
    
    if selector == 3:
        print("Equação: f(x) = √x + (x/2) + x^x")
        x = float(input("Digite o x: "))
        y = float(x/2)
        z = float(x ** x)
        w = float(x ** 0.5)
        x = y + w + z
        print("Resultado: ", x)
        break
    
    elif selector == 4:
        print("Troca de variáveis")
        x = int(input("Digite o X: "))
        y = int(input("Digite o Y: "))
        x, y = y, x
        print("Novo X: ", x)
        print("Novo Y: ", y)
        break

    elif selector == 5:
        print("Cálculo e diagnóstico de triângulo: ")
        a = int(input("Insira o lado A: "))
        b = int(input("Insira o lado B: "))
        c = int(input("Insira o lado C: "))
        s = int((a+b+c)/2)
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        
        if a != b and a != c and b != c:
            print("O triângulo é escaleno")
            print("A área do triângulo, com base na fórmula de Heron, é: ", area)
            break
        elif a == b and a == c and b == c:
            print("O triângulo é equilátero")
            print("A área do triângulo, com base na fórmula de Heron, é: ", area)
            break
        else:         
            print("O triângulo é isósceles")
            print("A área do triângulo, com base na fórmula de Heron, é: ", area)
            break
    
    elif selector == 6:
        #Não, pois ele vai printar duplicadamente se maior que 100 e independentemente par ou ímpar
        a = int (input("Digite um número: "))
        if a % 2 == 0 and a < 100:
            print ("O número é par e menor do que 100")
            #break
        else:
            if a >= 100:
                #and a % 2 == 0
                print ("O número é par e maior ou igual que 100")
                #break
            if a % 2 != 0 and a < 100:
                print ("O número é ímpar e menor do que 100")
                #break
            else:
                    if a >= 100:
                        #and a % 2 != 0
                        print ("O número é ímpar e maior ou igual que 100")
                        #break
    
    elif selector == 7:
        print("Conversor de temperaturas")
        tinputchar = (input("Digite se a temperatura lida é em Fahrenheit (F) ou Celsius (C): "))
        tinput = int(input("Digite os graus da temperatura: "))
        if tinputchar == 'C' or tinputchar == 'Celsius':
            print("Escala de temperatura escolhida: Celsius")
            tinput = (tinput * 9/5) + 32 
            print("Temperatura em Fahrenheits: ", tinput)
            break
        elif tinput == 'F' or tinputchar == 'Fahrenheit' or tinputchar == 'Fahrenheits':
            print("Escala de temperatura escolhida: Fahrenheit")
            tinput = (tinput - 32) * 5/9
            print("Temperatura em Celsius: ", tinput)
        else:
            print("Não entendi. Encerrando programa...")
            quit
        
    elif selector == 8:
        print("Identificador de anos bissextos")
        ano = int (input("Coloque o ano desejado (formato xxxx): "))
        if ano % 400 == 0:
            print("O ano é bissexto")
            break
        elif ano % 4 == 0 and ano % 100 != 0:
            print("O ano é bissexto")
            break
        else:
            print("O ano não é bissexto")
            break
    
    elif selector == 9:
        print("Verificador de aposentadoria")
        sexo = (input("Digite seu sexo (M/F): "))
        idade = int(input("Digite sua idade (anos): "))
        tmpcon = int(input("Digite seu tempo de contribuição (anos): "))
        if sexo == 'M' and idade >= 65 and tmpcon >= 10:
            print("Aposentável")
            break
        elif sexo == 'M' and idade >= 63 and tmpcon >= 15:
            print("Aposentável")
            break
        elif sexo == 'F' and idade >= 63 and tmpcon >= 10:
            print("Aposentável")
            break
        elif sexo == 'F' and idade >= 61 and tmpcon >= 15:
            print("Aposentável")
            break
        else:
            print("Não aposentável")
            break
    
    elif selector == 10:
        print("Calculadora")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        sinal = (input("Digite o sinal (+ ou - ou * ou /): "))
        if sinal == '+':
            n1 += n2
            print("Resultado da soma: ", n1)
            break
        elif sinal == '-':
            n1 -= n2
            print("Resultado da subtração: ", n1)
            break
        elif sinal == '*':
            n1 *= n2
            print("Resultado da multiplicação: ", n1)
            break
        elif sinal == '/':
            n1 /= n2
            print("Resultado da divisão: ", n1)
            break
    
    else:
        print("Erro! Fechando o programa...")
        quit