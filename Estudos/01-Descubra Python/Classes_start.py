# exemplo de como criar classes

class minha_classe():
    def __init__(self):
        self.meu_atributo = "Passou pelo construtor"
    
    def meu_metodo(self):
        print("Passou pelo meu metodo")

    def meu_metodo2(self, valor):
        self.outro_atributo = valor 
        print(self.outro_atributo)

def criar_objeto():
    meu_obj = minha_classe()
    var1 = meu_obj.meu_atributo
    print(var1)

    meu_obj.meu_metodo()

    meu_obj.meu_metodo2("Executando um método")

criar_objeto()