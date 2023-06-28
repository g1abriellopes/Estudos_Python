
# definindo uma função basica
def func1():
    print("Eu sou uma função")
func1()

# função que recebe argumentos
def Func2(arg1, arg2):
    print(arg1 + " " + arg2)

Func2("Dani", "Monteiro")

# função que retorna um valor
def cubo(x):
    return x * x * x

f = cubo(3)
print(f)
print(cubo(2))
