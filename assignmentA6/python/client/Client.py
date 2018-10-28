import socket

def fileTransfer(sock):
    fileName = input('Enter Name of File to Receive : ')
    sock.send(bytes(fileName, encoding = 'UTF-8'))
    with open(fileName , 'wb') as file:
        file.write(sock.recv(65535))

def calculator(sock):
    sock.send(bytes(input('1: addition\n2: substraction\n3: multiplication\n4: division\n>') , encoding = 'UTF-8'))
    sock.send(bytes(input('Enter 1st Number : ') , encoding = 'UTF-8'))
    sock.send(bytes(input('Enter 2nd Number : ') , encoding = 'UTF-8'))
    print('Answer : ' , sock.recv(8).decode(encoding = 'UTF-8'))

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',5000))

    choice = input('1: Echo Message\n2: File Transfer\n3: Calculator\n>')
    sock.send(bytes(choice, encoding = 'UTF-8'))

    if choice == '1':
        sock.send(bytes(input('Enter Message to Send : '), encoding = 'UTF-8'))
        print('Received message' , sock.recv(65535).decode(encoding = 'UTF-8'))
    elif choice == '2':
        fileTransfer(sock)
    elif choice == '3':
        calculator(sock)

    sock.close()
