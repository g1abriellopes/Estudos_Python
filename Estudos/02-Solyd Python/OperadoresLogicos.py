# comparacoes: ==,  !=, >, <, >=, <= 

var_verdade = True
var_falso = False

print(type(var_verdade), type(var_falso))

if var_verdade == True:
    print('Var verdade é verdadeiro')


print('Menu:\n1 = Escreve guilherme\n2 = escreve joao \n3 = escreve maria')

opcao = input ('Escolha uma opcao:')

if opcao == '1' :
    print('Guilherme')
elif opcao == '2' :
    print('Joao')
elif opcao == '3' :
    print('Maria')
else:
    print('Nenhuma das opcoes')


idade = int(input ('Escreva sua idade:'))
peso = float(input('Escreva seu peso:'))
altura = float(input('Escreva sua altura'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce esta apto a servir o exercito')
else:
    print('voce não esta apto')