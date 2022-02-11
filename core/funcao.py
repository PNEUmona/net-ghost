import requests as r
import whois11 as w
import os as o
import sys as s


def ping(alvo):
    print(o.system(f'ping -c 2 -w 2 {alvo}'))


def fping(alvo):
    print(o.system(f'fping -c 2 -w 2 {alvo}'))


def nmap(alvo):
    print()


def theharvester(alvo):
    lista = []
    print()


def dnsenum(alvo):
    print()


def dirb(alvo):
    print()


def host(alvo):
    print()
