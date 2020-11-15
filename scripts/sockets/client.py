import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = False

def handleServer():
    global connected

    while connected:
        message = client.recv(2048).decode(FORMAT)
        print(message)

def main():
    global connected
    connected = True

    thread = threading.Thread(target = handleServer)
    thread.start()

    while True:
        message = input('Message: ')
        if len(message) > 0:
            client.send(message.encode(FORMAT))
        else:
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))
            connected = False
            break

if __name__ == '__main__':
	main()