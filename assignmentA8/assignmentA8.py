import socket
import os

if __name__ == '__main__' :
    while True:
        choice = input('\n\n\nEnter choice\n1 : Name to Address\n2 : Address to Name\n3 : NSLOOKUP\n4 : Exit\n> ')
        if choice == '1':
            try:
                print('Address : ',socket.gethostbyname(input('Enter Name of Host    : \n> ')))
            except Exception as e:
                print(e)
        elif choice == '2':
            try:
                print('Name    : ',socket.gethostbyaddr(input('Enter address of Host : \n> ')))
            except Exception as e:
                print(e)
        elif choice == '3':
            try:
                os.system('nslookup ' + input('Enter URL / IP address : '))
            except Exception as e:
                print(e)
        else:
            break
