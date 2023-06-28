# imprimindo frase pulando caracteres

frase = 'Oi, tudo bem?'

lista_nomes = ['joao', 'maria', 'jose', 'carlos']

print(lista_nomes[0:3:2])

print(lista_nomes[-1]) # imprime o ultimo da lista

print(frase[0:13:2])

lista_nomes.append('geralda') # adiciona na lista
lista_nomes.remove('joao') # remover da lista
lista_nomes[0] = 'Robervania' #alterada o item 0 para o que foi definido
print(lista_nomes.pop()) #retira o ultimo nome da lista


frase_separada = frase.split(',') # separa a string transformando em uma lista

print(frase_separada)