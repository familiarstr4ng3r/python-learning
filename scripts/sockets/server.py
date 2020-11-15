import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
#print (SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def sendAll(fromClient, message):
    for c in clients:
        if c == fromClient:
           	continue

        message = message.encode(FORMAT)
        c.send(message)

def handleClient(conn, addr):
    print (f'New connection: {addr}')
    clients.append(conn)

    connected = True
    while connected:
        message = conn.recv(2048).decode(FORMAT)

        if message == DISCONNECT_MESSAGE:
            connected = False
            clients.remove(conn)

        message = f'{addr}: {message}'

        sendAll(conn, message)

        print(message)

    conn.close()

def main():
    print('Server started')
    server.listen()
    print(f'Servet listening {ADDR}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()

if __name__ == '__main__':
    main()
