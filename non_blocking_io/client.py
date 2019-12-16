import socket

MAX_CONNECTIONS = 20
address_to_server = ('localhost', 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address_to_server)
client.send(bytes("post ex.txt", encoding='UTF-8'))
data = client.recv(1024)
print(str(data))