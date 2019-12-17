import socket

MAX_CONNECTIONS = 20
address_to_server = ('localhost', 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address_to_server)
client.send(bytes("post http://127.0.0.1:8080/ex.txt HTTP/1.1", encoding='UTF-8'))
data = client.recv(1024)
print(str(data))