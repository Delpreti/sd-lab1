# Lado passivo/server

import socket

HOST = ''     # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5000  # porta onde chegarao as mensagens para essa aplicacao

with socket.create_server((HOST, PORTA)) as s:
    s.listen(5)
    print(f"Server started, listening on port {PORTA}")
    conn, addr = s.accept()
    with conn:
        print("Accepted connection from", addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
