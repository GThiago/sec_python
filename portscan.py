# -*- coding: utf-8 -*-
import socket


fp = raw_input('Digite o IP ou endereço: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.1)
client.connect_ex((fp, 80))

for port in range(10,1024):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.02)
    code = client.connect_ex((fp, port)) #conecta e tras o retorno

    if code == 0:
        print ('porta ' + str(port) + ': aberta!')

print('Concluido Scan!')