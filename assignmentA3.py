
import math
import argparse
from subprocess import Popen,PIPE
import platform

def pingIP(args):

    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + args.ip
    need_sh = False if  platform.system().lower()=="windows" else True
    proc = Popen(args, shell=need_sh , stderr = PIPE , stdout = PIPE )
    out , err = proc.communicate()
    exitCode = proc.returncode
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    s = "Ping unsuccessful : "
    if exitCode == 0:
        print("PING Successful")
    elif "Destination Host Unreachable" in out:
        print(s + "Destination Host Unreachable")
    elif "Request Timed Out" in out:
        print(s + "Request Timed Out") 
    else:
        print(s)
        


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
    elif n in range(24,32):
        submask[0] = 255
        submask[1] = 255
        submask[2] = 255
        submask[3] = sum([2**( 7 - x ) for x in range(n - 24) ])
    return submask




def findSubnetMask(args):    
    i = str(args.ip).split('/')
    ip = i[0].split('.')
    ip = [int(x) for x in ip]

    if len(ip) > 4:
        print('Invalid ip address')
        return

    if('/' in args.ip and args.s == None):
        print('CIDR')
        print( 'Subnet Mask = ' , cidrSubnetMask(ip,int(i[1])) )


    elif('/' not in args.ip):
        print('Classfull')
        cl = ""
        n = 0
        if args.s == None:
            args.s = 1 
        try:
            n = math.ceil(math.log2(args.s))
        except ValueError:
            print('No. of Subnets cannot be 0')
            return
            
        
        if ip[0] in range(1,128):
            cl = 'A'
            if args.s < 2**24 :
                l = cidrSubnetMask(ip,n+8)
                print( 'Class = ' , cl , 'Subnet mask = ' , l)
            else:
                print('Invalid No. of Subnets')
        
        elif ip[0] in range(128,192):
            cl = 'B'
            if args.s < 2**16 :
                print( 'Class = ' , cl , 'Subnet mask = ' ,cidrSubnetMask(ip,n+16) ),
            else:
                print('Invalid No. of Subnets')
            
        elif ip[0] in range(192,224):
            cl = 'C'
            if args.s < 2**8 :
                print( 'Class = ' , cl , 'Subnet mask = ' ,cidrSubnetMask(ip,n+24) ),
            else:
                print('Invalid No. of Subnets')

    else:
        print('Invalid Format')



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
    args = parser.parse_args()
    args.func(args)
