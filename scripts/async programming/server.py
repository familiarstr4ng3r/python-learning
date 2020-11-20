import socket

ADDR = ('localhost', 5050)
FORMAT = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(ADDR)
server_socket.listen()

while True:
	print('Before accept')
	client_socket, addr = server_socket.accept()
	print('Connection from', addr)

	while True:
		request = client_socket.recv(4096)

		if not request:
			break
		response = 'Hello world\n'.encode(FORMAT)
		client_socket.send(response)

	print('Outside')
	client_socket.close()