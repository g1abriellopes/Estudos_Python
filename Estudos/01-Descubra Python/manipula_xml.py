import xml.dom.minidom 

def manipula_xml():
    doc = xml.dom.minidom.parse("S:\\BI\\19. Desenvolvimentos\\Codigos\\Códigos\\Outros\\Cursos Python\\Descubra Python\\exemploXML.xml")

    print("Nome da primeira tag: ", str(doc.firstChild.tagName))
    primeiro_nome = doc.getElementsByTagName("firstname")
    print("o primeiro nome é: ",primeiro_nome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print("skill encontrada :", skill.getAttribute("name"))

manipula_xml()