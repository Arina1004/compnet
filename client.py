import socket
SERVER = "127.0.0.1"
PORT = 8080
HEADER_LENGTH = 10
# # my_username = input("Username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
# username = my_username.encode('utf-8')
# client.sendall(username)
# client.sendall(bytes("This is from Client",'UTF-8'))
while True:
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  in_data =  client.recv(1024)
  print("From Server :" ,in_data.decode())
  if out_data=='bye':
    break
client.close()