import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)
sock.bind(server_address)

fileName , clientAddress = sock.recvfrom(256)
with open(fileName.decode(encoding = 'UTF-8') , 'rb') as file:
    sock.sendto(file.read(65535), clientAddress)

sock.close()
