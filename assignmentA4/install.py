import os

os.system('ssh -t root@{} yum install nasm -y'.format(input('Enter IP address of machine')))
