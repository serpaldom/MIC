#!/usr/bin/env python

from OTXv2 import OTXv2
import argparse
import get_malicious
import hashlib
import os

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# Your API key
API_KEY = ''
OTX_SERVER = 'https://otx.alienvault.com/'
otx = OTXv2(API_KEY, server=OTX_SERVER)

parser = argparse.ArgumentParser(description='OTX CLI Example')
parser.add_argument('-ip', help='IP eg; 4.4.4.4', required=True)
parser.add_argument('-m', help=' 1 print all \n 2 only print probably and malicious IP', required=True)


args = vars(parser.parse_args())
mode = int(args['m'])

if args['ip']:
    alerts = get_malicious.ip(otx, args['ip'])
    if mode == 1:
        if len(alerts) == 0:
            print(bcolors.OK + str(args['ip']) + ' is NOT malicious by OTX ['+str(len(alerts))+' pulses detected]' + bcolors.RESET)
        if len(alerts) > 0 and len(alerts) <= 5:
            print(bcolors.WARNING + str(args['ip']) + ' is probably malicious by OTX ['+str(len(alerts))+' pulses detected]' + bcolors.RESET)
        if len(alerts) > 5:
            print(bcolors.FAIL + str(args['ip']) + ' is malicious by OTX ['+str(len(alerts))+' pulses detected]' + bcolors.RESET)
    if mode == 2:
        if len(alerts) > 0 and len(alerts) <= 5:
            print(bcolors.WARNING + str(args['ip'])+ bcolors.RESET)
        if len(alerts) > 5:
            print(bcolors.FAIL + str(args['ip'])+ bcolors.RESET)




