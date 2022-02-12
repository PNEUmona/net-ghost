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
    try:
        os.system('cls')
    except:
        os.system('clear')
    else:
        banner = "\n" + cores.VERDE + """	
        _    __      ___                __      __           
        | |  / /_  __/   |  ____  ____ _/ /_  __/ /___________
        | | / / / / / /| | / __ \/ __ `/ / / / / __/ ___/ ___/
        | |/ / /_/ / ___ |/ / / / /_/ / / /_/ / /_/ /__(__  ) 
        |___/\__,_/_/  |_/_/ /_/\__,_/_/\__, /\__/\___/____/  
                                    /____/                 """ + cores.BRANCO + """
                            \033[1;97m	--NETWORK SCAN"""
        
        print(banner)
        parse = argparse.ArgumentParser(description='-d')
        argsf = parse.parse_args()
        if sys.argv[1] == '' or sys.argv[1] == "--help":
            descricao = """
                MODO DE USAR python3 VuAnalytics.py 0.0.0.0/0
            """
            print(descricao)

            ###TRACEROUT
            #def
            #result, unans = traceroute(ip, maxttl=64)
            #for snd, rcv in result:
            #    print snd.ttl, rcv.src, snd.sent_time, rcv.time




if __name__ == "__main__":
    main()
