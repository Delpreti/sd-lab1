# Lado ativo/client

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000       # porta que o par passivo esta escutando

with socket.create_connection((HOST, PORTA)) as s:
    while True:
        message = input()
        if message == "exit":
            break
        s.sendall(bytes(message, 'utf-8'))
        print(str(s.recv(1024),  encoding='utf-8'))
