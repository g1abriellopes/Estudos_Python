# escrevendo arquivo com funcoes do Python

#w+ escreve (w) e se não existir o arquivo ele será criado (+)
# \r\n pula uma linha


def escreve_arquivo():
    arquivo = open("novo_arquivo.txt", "w+")
    
    arquivo.write("Linha gerada com a funcao 'escreve_arquivo' \r\n")

    arquivo.close()

#escreve_arquivo()

def altera_arquivo():
    arquivo = open("novo_arquivo.txt", "a+")
    
    arquivo.write("Linha gerada com a funcao 'escreve_arquivo' \r\n")

    arquivo.close()

altera_arquivo()


