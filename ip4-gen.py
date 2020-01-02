#!/usr/bin/python3
import random,os,re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

reg_ipv4 = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

def clean():
    os.system('cls' if os.name=='nt' else 'clear')

def logo():
    print('''                                                                     
                   {}╔══╗     ╔╗ ╔╗                                                            
                   ╚╣╠╝     ║║ ║║                                                            
                    ║║╔══╦╗╔╣╚═╝║  ╔══╦══╦═╗                                                 
                    ║║║╔╗║╚╝╠══╗╠══╣╔╗║║═╣╔╗╗                                                
                   ╔╣╠╣╚╝╠╗╔╝  ║╠══╣╚╝║║═╣║║║                                                
                   ╚══╣╔═╝╚╝   ╚╝  ╚═╗╠══╩╝╚╝                                                
                      ║║           ╔═╝║                                                      
                      ╚╝           ╚══╝                                                      
                   {}|#| Wilaia Shield Team |#|                                                                          
                   {}B{}adr {}A{}zeez fb.com/linux.2.0.1.4{}
'''.format(bcolors.HEADER,bcolors.WARNING,bcolors.OKBLUE,bcolors.FAIL,bcolors.OKBLUE,bcolors.FAIL,bcolors.ENDC))

def help_msg():
    clean()
    logo()
    print('''{}1- Generate Random IP Addresses
\t|__this will generate random ipv4\n\t|__Example set value 10 will generat\n\t|__92.48.58.2\n\t|__50.21.02.100\n\t|__etc...\n
2- Generate Range IP Addresses
\t|__this will generate manual ipv4\n\t|__Example set start ip 100.100.100.1 and set end ip 100.100.254.25 will generat\n\t|__100.100.100.1\n\t|__100.100.100.2\n\t|__etc 100.100.254.25\n
3- Exit\n{}'''.format(bcolors.WARNING,bcolors.ENDC))


def randoms(num, save='output.txt'):
    clean()
    logo()
    print(bcolors.OKGREEN+'|+|'+bcolors.WARNING+' Create File Name '+bcolors.BOLD+save+bcolors.ENDC)
    with open(save, 'a+') as f:
        print(bcolors.OKGREEN+'|+|'+bcolors.WARNING+' Wait Append IPs To '+bcolors.BOLD+save+bcolors.ENDC)
        for cip in range(num):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            d = random.randint(0, 255)
            f.write('{}.{}.{}.{}\n'.format(a, b, c, d))
    f.close()
    print(bcolors.OKGREEN+'|+|'+bcolors.WARNING+' Generated'+bcolors.BOLD,num,bcolors.ENDC)
    exit(bcolors.OKGREEN+'|+| Finish')

def ranges(start, end, save):
    clean()
    logo()
    temp = start
    ip_range = []
    with open(save,'a+') as f:
        f.write(''.join(str(e) + '.' for e in start)[:-1]+'\n')
        print(bcolors.OKGREEN + '|+|' + bcolors.WARNING + ' Created File Name ' + bcolors.BOLD + save + bcolors.ENDC)
        print(bcolors.OKGREEN + '|+|' + bcolors.WARNING + ' Wait Append Range ' + bcolors.HEADER,
              ''.join(str(e) + '.' for e in start)[:-1] + '-' + ''.join(str(e) + '.' for e in end)[:-1], bcolors.WARNING + 'To ' + bcolors.BOLD + save + bcolors.ENDC)
        while temp != end:
            start[3] += 1
            for i in (3, 2, 1):
                if temp[i] == 256:
                    temp[i] = 0
                    temp[i - 1] += 1
            ip_range.append('.'.join(map(str, temp)))
            f.write('.'.join(map(str, temp))+'\n')
        print(bcolors.OKGREEN + '|+|' + bcolors.WARNING + ' Generated' + bcolors.BOLD, format(len(ip_range),',d'))
        exit(bcolors.OKGREEN + '|+| Finish')



def ran():
    try:
        num = int(input('How Many IP Addresses (Ex:100)->'))
        print('set ->', num)
        save = input('Output Path (Ex:/root/list.txt)->')
        randoms(num, save)
    except ValueError:
        print(bcolors.FAIL+bcolors.BOLD+'Value Error Set Valid Number'+bcolors.ENDC)
        ran()

def manu():
    start_ip = input('start ip->')
    end_ip = input('end ip->')
    if reg_ipv4.match(start_ip) and reg_ipv4.match(end_ip):
        start = list(map(int, start_ip.split('.')))
        end = list(map(int, end_ip.split('.')))
        if start[0] > end[0]:
            print(bcolors.FAIL + bcolors.BOLD + 'Value Error Have To Start IP Less Than End IP' + bcolors.ENDC)
            manu()
        save = input('Output Path->')
        ranges(start, end, save)
    else:
        print(bcolors.FAIL + bcolors.BOLD + 'Value Error Set Valid IPv4' + bcolors.ENDC)
        manu()

try:
    help_msg()
    t_method = input("Choose->")
    if t_method == '1':
        ran()
    elif t_method == '2':
        manu()
    elif t_method == '3':
        exit()
    else:
        help_msg()
        print(bcolors.FAIL + bcolors.BOLD + 'Value Error Choose 1,2,3' + bcolors.ENDC)
        exit()
except KeyboardInterrupt:
    exit('\nExit\n')