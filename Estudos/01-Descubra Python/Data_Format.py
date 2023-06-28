from datetime import datetime 

#y/%Y - Ano, %a/%A - Dia da semana, %b%B - Mês. %d - dia do mês

def formata_data_hora():
    hoje = datetime.now()

    print(hoje.strftime("o ano é: %y"))

    print(hoje.strftime("Data e hora local: %c"))

# %I/%H - 12/24 horas, %M - minuto, %S - segundos, %p - AM/PM

    print(hoje.strftime("A hora atual é: %I:%M:%S %p"))


formata_data_hora()