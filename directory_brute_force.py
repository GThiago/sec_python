import requests

domin = str(input('dominio: '))
url= 'http://' + domin + '/'

arquivo = open('/usr/share/dirb/wordlists/small.txt', 'r')
linhas = arquivo.readlines()

for linha in linhas :
    response = requests.get(url + linha)
    if response.status_code == 200:
        print(url + linha)
        