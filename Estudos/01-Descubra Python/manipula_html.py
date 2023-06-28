from html.parser import HTMLParser

class meu_parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print("Valores encontrados", a[0], " = ", a[1])
    
    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada")
    
    def handle_comment(self, data):
        print("comentario encontrado")
    
    def handle_data(self, data):
        print("Valores encontrados")
        if data.isspace():
            print("Valor encontrado é um espaço")
        else: 
            print("O valor encontrado é: ", data)

def meu_objeto():
    meu_parser1 = meu_parser()
    arquivo = open("S:\\BI\\19. Desenvolvimentos\\Codigos\\Códigos\\Outros\\Cursos Python\\Descubra Python\\exemplohtml.html", "r")
    dados = arquivo.read()
    meu_parser1.feed(dados)

meu_objeto()