import sqlite3 

def manipula_dados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def seleciona_dados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)

def manipulacao_dados():
    comando_insert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado testes', 'XXx', 'Teste Inclusãos')"
    pathBD = "S:\\BI\\19. Desenvolvimentos\\Codigos\\Códigos\\Outros\\Cursos Python\\Descubra Python\\BancoDeDados.db"
    comando_select = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipula_dados(pathBD, comando_insert)
    seleciona_dados(pathBD, comando_select)

manipulacao_dados()
