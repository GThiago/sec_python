import dns.resolver
import sys

arg = sys.argv
try:
	dominio = arg[1]
	nome_arq = arg[2]
	print(dominio, nome_arq)
except:
	print('arq <dominio> <worklist>')
	sys.exit(1)
try:
	arq = open(nome_arq)
	subdominios = arq.read().splitlines()
except:
	print('Arquivo no encontrado')
	sys.exit()

for subdominio in subdominios:
	try:
		domesub = subdominio + '.' + dominio
		resultados = dns.resolver.query(domesub,'a')
		for resultado in resultados:
			print (subdominio, resultado)
	except:
		pass

