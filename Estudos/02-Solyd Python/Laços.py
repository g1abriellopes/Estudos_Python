i = 0 
while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1 # também pode ser utilizado o 1 += 1 que é a mesma coisa

print('Acabou o while: ', i)

numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []

i = 1

while i <= int(numero_de_convidados):
    nome_do_convidado = input('Coloque o nome do convidado: #' + str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1 

print(lista_de_convidados)




