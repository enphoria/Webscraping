import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen('https://www.larepublica.co').read().decode()

soup = BeautifulSoup(data)
tags = soup('a')  # Aqui es la rama principal de donde lo extraemos de la página
for tag in tags:
    print(tag.get('href'))  # Aqui ponemos la subrama de lo que queremos extraer de la página
