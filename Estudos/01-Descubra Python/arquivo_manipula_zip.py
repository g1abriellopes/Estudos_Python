# exemplo como trabalhar com arquivos

import os 
from os import path 
import shutil 
from shutil import make_archive
from zipfile import ZipFile

def cria_zip():
    shutil.make_archive("arquivo_compactado", "zip", "S:\\BI\\19. Desenvolvimentos\\Codigos\\Códigos\\01 - Em Andamento\\BSB_215 - Gross Margin")

#cria_zip()

def cria_zip2():
    with ZipFile("arquivo_zip_modo2", "w") as novo_zip:
        novo_zip.write("arquivo_alterado.bkp")
        novo_zip.write("novo_arquivo.txt")

    

cria_zip2()