# Definindo um loop while

def loopwhile():
    x = 0 
    while (x < 5):
        print(x)
        x = x + 1

loopwhile()

# loop for em uma coleção

def loopArray():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for d in dias:
        print(d)

loopArray()


# usando a funcao enumerate, para buscar valores e seus indices

def loopEnum():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i, d in enumerate(dias):
        print(i,d)

loopEnum()