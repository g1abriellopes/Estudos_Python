
import urllib.request
import json 

def manipula_json():

    #acessar uma pagina
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web_url = urllib.request.urlopen(endereco)
    if (web_url.getcode() == 200):

    # busca os dados da pagina e grava em um objeto "oJSON"
        dados = web_url.read()
        oJSON = json.loads(dados)

    # navega no objeto e mostra algumas unformações
        contagem = oJSON["metadata"]["count"]
        print("contagem: " + str(contagem))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "293 km ENE of Kuril’sk, Russia":
                print("****Encontrado registro especial****")
            else:
                print(local["properties"]["place"])

manipula_json()









