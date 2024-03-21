from cryptofuzz import Bitcoin, Generator, Convertor
from colorama import Fore, Style
from typing import Optional
import json
import multiprocessing
from multiprocessing import Pool
import threading

koinhacker = '''

██╗░░██╗░█████╗░██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░██╔╝██╔══██╗██║████╗░██║██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████═╝░██║░░██║██║██╔██╗██║███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔═██╗░██║░░██║██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚██╗╚█████╔╝██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
--------------------------------------------------------
[x] Software: BTCxCRYPTOFUZZ
[x] Author: KoinHacker
[x] Github: koinhacker
[x] Version: 1.0
--------------------------------------------------------
Donate me BTC: bc1qhzems2lsstx795ae8er698zp0vvcvg3p39e3yr
========================================================

▀▀█▀▀ ░█▀▀█ ▀█▀ ─█▀▀█ ░█─── 　 ░█──░█ ░█▀▀▀ ░█▀▀█ ░█▀▀▀█ ▀█▀ ░█▀▀▀█ ░█▄─░█ 
─░█── ░█▄▄▀ ░█─ ░█▄▄█ ░█─── 　 ─░█░█─ ░█▀▀▀ ░█▄▄▀ ─▀▀▀▄▄ ░█─ ░█──░█ ░█░█░█ 
─░█── ░█─░█ ▄█▄ ░█─░█ ░█▄▄█ 　 ──▀▄▀─ ░█▄▄▄ ░█─░█ ░█▄▄▄█ ▄█▄ ░█▄▄▄█ ░█──▀█
'''

PRINT = Fore.GREEN + koinhacker + Fore.RESET
print('\n\n', Fore.RED, str(PRINT), Style.RESET_ALL, '\n')

r = 1
cores = 8

def finder(r):
    filename = "btc500.txt"
    with open (filename) as f: 
        add = f.read().split()
    add = set(add)
    
    conv = Convertor()
    gen = Generator()

    z = 1
    w = 0
    while True:
        private_key = gen.generate_private_key()
        seed = conv.hex_to_bytes(private_key)
        mnemonic = conv.hex_to_mne(private_key)

        btc = Bitcoin()

        # Generate addresses
        p2pkh = btc.hex_addr(private_key, "p2pkh")
        p2sh = btc.hex_addr(private_key, "p2sh")
        p2wpkh = btc.hex_addr(private_key, "p2wpkh")
        p2wsh = btc.hex_addr(private_key, "p2wsh")
        
        print('Winner Wallet:',Fore.GREEN, str(w), Fore.YELLOW,'Total Scan:',Fore.WHITE, str(z), Fore.YELLOW, Fore.YELLOW, 'P2PKH:', Fore.WHITE, str(p2pkh), Fore.YELLOW, 'P2SH:', Fore.WHITE, str(p2sh), Fore.YELLOW, 'P2WPKH:', Fore.WHITE, str(p2wpkh), Fore.YELLOW, 'P2WSH:', Fore.WHITE, str(p2wpkh), end='\r', flush=True)
        z += 1
                
        if p2pkh in add:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- BTC Address =', Fore.GREEN, str(p2pkh), end='\r')
            w += 1
            z += 1
            f = open("winner.txt", "a")
            f.write('\nAddress = ' + str(p2pkh))
            f.write('\nP2SH Address = ' + str(p2sh))
            f.write('\nP2WPKH Address = ' + str(p2wpkh))
            f.write('\nP2WSH Address = ' + str(p2wsh))
            f.write('\nPrivate Key = ' + str(private_key))
            f.write('\nMnemonic Phrase = ' + str(mnemonic))
            f.write('\n=========================================================\n')
            f.close()
            print('Winner information Saved On text file = ADDRESS ', str(p2pkh))
            continue

        
        
finder(r)

if __name__ == "__main__":
    with Pool(cores) as p:
        p.map(finder, range(cores))