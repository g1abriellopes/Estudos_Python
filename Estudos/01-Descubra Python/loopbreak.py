# como usar os comandos break e continue

def loopbreak():
    for x in range (5,10):
        if x == 7:
            break
        print("o valor de x é: ", x)
#loopbreak() interrompe a execução

def loopcontinue():
    for x in range(5,10):
        if x == 7:
            continue
        print("O valor de x é: ", x)
#loopcontinue() interrompe uma execução
