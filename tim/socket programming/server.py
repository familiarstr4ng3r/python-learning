# https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket
import threading

HEADER = 64
PORT = 5050
SERVER = '192.168.1.5'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f'New connection: {addr} connected')

    connected = True
    while connected:
        messageLength = conn.recv(HEADER).decode(FORMAT)
        if messageLength:
            messageLength = int(messageLength)
            message = conn.recv(messageLength).decode(FORMAT)

            if message == DISCONNECT_MESSAGE:
                connected = False

            print(f'{addr}: {message}')
            conn.send(f'Server received: {message}'.encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f'Listening {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()
        print(f'Active connections: {threading.activeCount() - 1}')

print('Server started')
start()
