#!/usr/bin/env python3
#RECON SCRIPT
#with Tracing, ip block list, Network mapper, Hosts Scan 
import os
import argparse
import sys
#from scapy.layers.inet import traceroute


class cores:
    VERDE = '\033[92m'
    BRANCO = '\033[91m'
    DF = '\033[0m'
    #YELLOW = '\033[33m'

    def disable(self):
        self.VERDE = ''
        self.BRANCO = ''
        self.DF = ''


def main():
    """
    try:
        os.system('cls')
    except:
        os.system('clear')
    else:
    """    
    banner = "\n" + cores.VERDE + """	
    ███╗   ██╗███████╗████████╗     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
    ████╗  ██║██╔════╝╚══██╔══╝    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
    ██╔██╗ ██║█████╗     ██║       ██║  ███╗███████║██║   ██║███████╗   ██║   
    ██║╚██╗██║██╔══╝     ██║       ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
    ██║ ╚████║███████╗   ██║       ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
    ╚═╝  ╚═══╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
                                                                        """ + cores.BRANCO + """
                        \033[1;97m	--NETWORK SCAN"""
    
    parser = argparse.ArgumentParser(description='Flag')
    parser.add_argument('-d','--domain' , help = 'Domain name' , required=True)
    parser.add_argument('-o','--output' , help = 'Output file name [by default it is \'domain.txt\']')
    args = parser.parse_args()
    manual = """
        MANUAL
    """

    print(banner)
    parse = argparse.ArgumentParser(description='-d')
    args = parse.parse_args()
    if args.damain:
        return args.damain

        print(descricao)
    if arg.output:
        print("save{}")
        ###TRACEROUT
        #def
        #result, unans = traceroute(ip, maxttl=64)
        #for snd, rcv in result:
        #    print snd.ttl, rcv.src, snd.sent_time, rcv.time




if __name__ == "__main__":
    main()