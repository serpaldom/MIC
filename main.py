import argparse
import os
import sys
parser = argparse.ArgumentParser(description='OTX CLI Example')
parser.add_argument('-f', help='-f filename.txt', required=True)
parser.add_argument('-mode', help=' 1 print all \n 2 only print probably and malicious IP', required=True)
args = vars(parser.parse_args())
filename = open(args['f'])
m = args['mode']
for ip in filename:
    os.system('python3 is_malicious.py'+ ' -m ' +  str(m) +' -ip ' + str(ip) )
