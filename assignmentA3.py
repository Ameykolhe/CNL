
import math
import argparse
from subprocess import Popen,PIPE
import platform
import ipaddress
import os

def pingIP(args):

    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + args.ip
    need_sh = False if  platform.system().lower()=="windows" else True
    proc = Popen(args, shell=need_sh , stderr = PIPE , stdout = PIPE )
    out , err = proc.communicate()
    exitCode = proc.returncode
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    s = "\nPing unsuccessful"
    print(exitCode)

    if ("Destination Host Unreachable" in out )  or ('Destination host unreachable' in out) :
        print(s + " : Destination Host Unreachable")
    elif "Request Timed Out" in out:
        print(s + " : Request Timed Out") 
    elif exitCode == 1:
        print(s + " : Host is Down")
    else:
        print("\nPING Successful\n")


def cidrSubnetMask(ip,n):
    submask = [0,0,0,0]
    if n in range(8):
        submask[0] = sum([2**( 7 - x ) for x in range(n) ])
    elif n in range(8,16):
        submask[0] = 255
        submask[1] = sum([2**( 7 - x ) for x in range(n - 8) ])
    elif n in range(16,24):
        submask[0] = 255
        submask[1] = 255
        submask[2] = sum([2**( 7 - x ) for x in range(n - 16) ])
    elif n in range(24,33):
        submask[0] = 255
        submask[1] = 255
        submask[2] = 255
        submask[3] = sum([2**( 7 - x ) for x in range(n - 24) ])
    return submask


def printDetail(*arg):
    if arg[0] != None:
        print("Class : " ,  arg[0])
    print("IP : " , arg[1] )
    print("NetId : " ,  arg[2])
    print("SubnetMask : ",arg[3] ,'\n')
    if arg[5] == True:
        #print(type(arg[4][0]))
        network = arg[4]
        ip = ipaddress.IPv4Address(str(arg[1]).split('/')[0])
        sno = 0
        fl = None
        print("SunbetNo\tStartAddress\t\tLastAddress")
        for sunbnetAddresses in network:
            sno += 1
            sunbnetAddresses = list(sunbnetAddresses)
            print("{}\t\t{}\t\t{}".format(sno,str(sunbnetAddresses[0]),str(sunbnetAddresses[-1])))
            if ip in sunbnetAddresses :
                fl = sno
        if fl != None :
            print('\n','Address : ',str(ip) ,'is present in Subnet no. : ' , fl,'\n')
    return arg
        


def findSubnetMask(args):    
    i = str(args.ip).split('/')
    ip = i[0].split('.')
    ip = [int(x) for x in ip]
    netId = [0,0,0,0]

    subnetting = True if args.s != None else False

    n = 0
    if args.s == None:
        args.s = 1 
    try:
        n = math.ceil(math.log2(args.s))
    except ValueError:
        print('\nNo. of Subnets cannot be 0')
        return

    if len(ip) > 4:
        print('\nInvalid ip address')
        return

    if('/' in args.ip):
        if args.s > 2**(32 - int(i[1])) :
            print("\nInvalid no. of Subnets")
            return
        print('\nClassless')
        l = cidrSubnetMask(ip,int(i[1]) + n)
        l = '.'.join(str(x) for x in l)
        ip = '.'.join(str(x) for x in ip)
        ip = ip + '/' + str(i[1])
        ip = ipaddress.ip_interface(ip)
        netId = ip.network
        if args.s != None:
            network = list(netId.subnets(n))
        return printDetail(None,ip,netId,l,network,subnetting)


    elif('/' not in args.ip):
        print('\nClassfull')
        cl = ""   
        
        if ip[0] in range(1,128):
            cl = 'A'
            netId[0] = ip[0]
            if args.s < 2**24 :
                l = cidrSubnetMask(ip,n+8)
                l = '.'.join(str(x) for x in l)
                ip = '.'.join(str(x) for x in ip)
                netId = '.'.join(str(x) for x in netId)
                netId = netId + '/' + str(8)
                netId = ipaddress.IPv4Network(netId)
                network = list(netId.subnets(n))
                return printDetail(cl,ip,netId,l,network,subnetting)
            else:
                print('\nInvalid No. of Subnets')
        
        elif ip[0] in range(128,192):
            cl = 'B'
            netId[0] = ip[0]
            netId[1] = ip[1]
            if args.s < 2**16 :
                l = cidrSubnetMask(ip,n+16)
                l = '.'.join(str(x) for x in l)
                ip = '.'.join(str(x) for x in ip)
                netId = '.'.join(str(x) for x in netId)
                netId = netId + '/' + str(16)
                netId = ipaddress.IPv4Network(netId)
                network = list(netId.subnets(n))
                return printDetail(cl,ip,netId,l,network,subnetting)
            else:
                print('\nInvalid No. of Subnets')
            
        elif ip[0] in range(192,224):
            cl = 'C'
            netId[0] = ip[0]
            netId[1] = ip[1]
            netId[2] = ip[2]
            if args.s < 2**8 :
                l = cidrSubnetMask(ip,n+24)
                l = '.'.join(str(x) for x in l)
                ip = '.'.join(str(x) for x in ip)
                netId = '.'.join(str(x) for x in netId)
                netId = netId + '/' + str(24)
                netId = ipaddress.IPv4Network(netId)
                network = list(netId.subnets(n))
                return printDetail(cl,ip,netId,l,network,subnetting)
            else:
                print('\nInvalid No. of Subnets')

    else:
        print('\nInvalid Format')



def setIP(args):

    tparser = argparse.ArgumentParser()
    tparser.add_argument('-ip', type = str , help = 'ip' , required = True )
    tparser.add_argument('-s' , type = int , default = None , help = 'no of Subnets')
    temp = parser.parse_args( ['findSubnetMask','-ip',args.ip,'-s',str(args.s)])

    tup = temp.func(temp)
    try:
        os.system("sudo ifconfig " + args.interface + ' down')
        os.system("sudo ifconfig " + args.interface + ' ' + tup[1] + ' netmask ' + tup[3] )
        os.system("sudo ifconfig " + args.interface + ' up')
        print("IP address Updated Successfully")
    except Exception as e:
        print(e)



if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    subParser = parser.add_subparsers()

    pingParser = subParser.add_parser('PING')
    pingParser.add_argument('-ip', type = str , help = 'ip' , required = True )
    pingParser.set_defaults(func = pingIP)

    sNetParser = subParser.add_parser('findSubnetMask')
    sNetParser.add_argument('-ip', type = str  , help = 'ip' , required = True)
    sNetParser.add_argument('-s' , type = int , default = None , help = 'no of Subnets')
    sNetParser.set_defaults(func = findSubnetMask)
    
    setIPParser = subParser.add_parser('setIP')
    setIPParser.add_argument('-ip', type = str  , help = 'ip' , required = True)
    setIPParser.add_argument('-s' , type = int , default = 1 , help = 'no of Subnets')
    setIPParser.add_argument('-interface',type = str , help = 'Interface Name' , required = True)
    setIPParser.set_defaults(func = setIP)

    args = parser.parse_args()
    args.func(args)
