import socket
import threading
import os
import time

clientList = []

class Chat_Server:
    def __init__(self, address1 , address2 , port_number):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('192.168.0.100', port_number)
        self.server.bind(self.server_address)
        self.address1 = address1
        self.address2 = address2

    '''
    def get_clients(self):
        self.name1, self.address1 = self.server.recvfrom(4096)
        self.name2, self.address2 = self.server.recvfrom(4096)
        print('Address1 {} Address2 {}'.format(self.address1, self.address2))
        print('Initiated chat')
    '''


    def send1(self):
        print('Started thread1')
        while True:
            message, address = self.server.recvfrom(4096)
            print('Msg {} from {}'.format(message, address))

            if address == self.address1:
                self.server.sendto(message, self.address2)
            elif address == self.address2:
                self.server.sendto(message, self.address1)
            else:
                pass


    def send2(self):
        print('Started Thread2')
        while True:
            message, address = self.server.recvfrom(4096)
            print('Msg {} from {}'.format(message, address))

            if address == self.address1:
                self.server.sendto(message, self.address2)
            elif address == self.address2:
                self.server.sendto(message, self.address1)
            else:
                pass


    def run(self):
        self.thread1 = threading.Thread(target=self.send1, args=())
        self.thread2 = threading.Thread(target=self.send2, args=())

        self.thread1.start()
        self.thread2.start()

        self.thread1.join()
        self.thread2.join()


def get_clients(lock):
    global clientList

    clientListServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientListServer.bind(('192.168.0.100',5000))

    while True:
        name , address = clientListServer.recvfrom(4096)
        lock.acquire()
        clientList.append((name,address))
        print("ClientList : ",clientList)
        lock.release()


def main():
    global clientList

    matchserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    matchserver.bind(('192.168.0.100',5001))

    lock = threading.Lock()

    portno = 6000
    
    thread1 = threading.Thread(target=get_clients , args=(lock,))
    thread1.start()

    chatServerList = []

    while True:
        '''
        print(clientList)
        time.sleep(1)
        '''
        print("In Matching")
        name2 , address1 = matchserver.recvfrom(4096)
        print("Request Received From : ",address1)
        address2 = None
        name1 = None
        lock.acquire()
        print('***')
        for x , y in clientList :
            if y == address1:
                name1 = x
            if x == name2:
                address2 = y
        print('***')
        lock.release()
        print("Name  : {} with Name : {} Port : {} ".format(name1,name2,portno))

        matchserver.sendto(bytes(str(portno),encoding='UTF-8'),address1)
        matchserver.sendto(bytes(str(portno),encoding='UTF-8'),address2)

        chatServer = Chat_Server(address1,address2,portno)
        threading.Thread(target=chatServer.run , args=()).start()

        chatServerList.append(chatServer)
        portno = portno + 1 



if __name__ == '__main__':
    main()





'''

def main():
    # Test 1
    cs = Chat_Server(5000)
    cs.get_clients()
    cs.run()


    #test2

    #Change the port number in the Client_primary.py and Client_secondary.py respectively 
    cs1, cs2, cs3 = Chat_Server(5000), Chat_Server(5001), Chat_Server(5002)
    cs1.get_clients()
    cs2.get_clients()
    cs3.get_clients()
    main_thread1 = threading.Thread(target=cs1.run, args=())
    main_thread2 = threading.Thread(target=cs2.run, args=())
    main_thread3 = threading.Thread(target=cs3.run, args=())
    main_thread1.start()
    main_thread2.start()
    main_thread3.start()
    main_thread1.join()
    main_thread2.join()
    main_thread3.join()

    '''