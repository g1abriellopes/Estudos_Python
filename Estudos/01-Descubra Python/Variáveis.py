# Declarando uma variável
f = 0
print(f)

# Declarando a mesma variável
f = "abc"
print(f)

# Gerando um erro com variáveis diferente

print("isto é uma string" + str(123))

# Variavel Global x Variável local
def AlgumaFuncao():
    global f 
    f = "def"
    print(f)

AlgumaFuncao()
print(f)

# se não definir como variável global a função não será
# executada levando em consideração o que foi definido
# fora da função mas apenas o que está dentro dela

