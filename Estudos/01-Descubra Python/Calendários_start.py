# arquivo de exemplo de uso de calendários

import calendar 

# criando um calendario no formato texto

def calendario_texto():
    calendario_texto = calendar.TextCalendar(calendar.SUNDAY)
    txt_calendario = calendario_texto.formatmonth(2019, 6)
    print(txt_calendario)

#calendario_texto()

# criando um calendario no formato html 

def calendario_html():
    calendario_html = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendario = calendario_html.formatmonth(2019, 6)
    print(html_calendario)

#calendario_html()

def imprime_mes():
    for mes in calendar.month_name:
        print(mes)
    
    for dia in calendar.day_name:
        print(dia)

imprime_mes()
