import urllib3

url = 'http://g1.globo.com'

http = urllib3.PoolManager()
resposta = http.request('GET', url)

print(resposta.data)