# lendo arquivos com funções 


def leitura_arquivo():
    arquivo = open("novo_arquivo.txt", "r")
    if (arquivo.mode == "r"): # somente continua o codigo se o arquivo estiver em modo de leitura
        conteudo = arquivo.read()
        print(conteudo)
    
    arquivo.close()

#leitura_arquivo()

def leitura_arquivo_grande():
    arquivo = open("novo_arquivo.txt", "r")
    if (arquivo.mode == "r"): # somente continua o codigo se o arquivo estiver em modo de leitura
        conteudo_total = arquivo.readlines()

        for conteudo in conteudo_total:
            print(conteudo)
        
    arquivo.close()
    
leitura_arquivo_grande()