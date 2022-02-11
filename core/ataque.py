from pyrsistent import v
from funcao import *
import sys as s

x = s.argv[1]

print('======== Selecione uma função ========')
print()
print('1 --> PING')
print('2 --> FPING')
print('3 --> NMAP')
print('4 --> THEHARVESTER')
print('5 --> DNSENUM')
print('6 --> DIRB')
print('7 --> HOST')
escolha = input('Digite um numero: ')
print()

if escolha == '1':
    ping(x)

elif escolha == '2':
    fping(x)
    
elif escolha == '3':
    nmap(x)

elif escolha == '4':
    theharvester(x)

elif escolha == '5':
    dnsenum(x)

elif escolha == '6':
    dirb(x)

elif escolha == '7':
    host(x)

else:
    print('Voce digitou errado')
