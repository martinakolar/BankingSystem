import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect = for online sites, public ip
client.connect(("localhost", 9999))


message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(input(message).encode())
#fail or success
print(client.recv(1024).decode())