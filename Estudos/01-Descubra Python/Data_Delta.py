from datetime import date 
from datetime import time 
from datetime import datetime
from datetime import timedelta

def delta_tempo():
    delta  = timedelta( days = 86, hours=8532, minutes=7645)
    print(delta)
    hoje = datetime.now()

    print("data no futuro: ", hoje + delta)
    print("Data no passado: ", hoje - delta)

delta_tempo()
