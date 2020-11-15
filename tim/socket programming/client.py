import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.1.5'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    message = message.encode(FORMAT)
    messageLength = len(message)
    sendLength = str(messageLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    message = input('Write message or leave empty to disconnect:')
    if len(message) > 0:
        send(message)
    else:
        send(DISCONNECT_MESSAGE)
        break

#send('Hello World!')
#send(DISCONNECT_MESSAGE)

#s = socket.gethostbyname(socket.gethostname())
#print(s)
