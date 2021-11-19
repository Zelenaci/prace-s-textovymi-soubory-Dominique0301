#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:8.11.2021
# Autor:Dominik Šlehofer
############################################################################
from random import randint, choice

############################################################################

samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"



def mala():
    try:
        f1=open(input("Zadejte název vstupního souboru:"),"r")
    except FileNotFoundError:
        print("Soubor nenalezen!")
    
    try:
        f2=open(input("Zadejte název výstupního souboru:"),"w")
    except FileNotFoundError:
        print("Soubor nenalezen!")

    text = f1.read().lower()
    f2.write(text)

    f1.close()
    f2.close()


pocet={}


def stat():

    try:
        f1=open(input("Zadejte název vstupního souboru:"),"r")
    except FileNotFoundError:
        print("Soubor nenalezen!")
    
    while True:
        pismeno=f1.read(1)
        if pismeno=="":
            break

        if pismeno.isalpha():
            if pismeno not in pocet.keys():
                pocet[pismeno]=1
            else:
                pocet[pismeno]+=1
    f1.close()
    nej=max(pocet.values())
    for key in sorted(pocet.keys()):
        print("({0})->{1:2} | {2}".format(key, pocet[key], 20*pocet[key]//nej*"#"))


def znaky():
    try:
        f1=open(input("Zadejte název vstupního souboru:"),"r")
    except FileNotFoundError:
        print("Soubor nenalezen!")
    
    try:
        f2=open(input("Zadejte název výstupního souboru:"),"w")
    except FileNotFoundError:
         print("Soubor nenalezen!")
    while True:
        znak = f1.read(1)
        if znak=="":
            break
        if znak == "A":
            znak="&"
        f2.write(znak)
    f1.close()
    f2.close()



def gen_slov(minchars=1, maxchars=10):
    vysledek = ""
    pocet = randint(minchars, maxchars)
    if pocet == 1:  
        zacatek = 0
    else:
        zacatek = randint(0, 1)
    for i in range(pocet):
        if i % 2 == zacatek:
            vysledek = vysledek + choice(souhlasky)
        else:
            vysledek = vysledek + choice(samohlasky)
            if randint(1, 10) == 1: 
                vysledek = vysledek + choice(samohlasky)
    return vysledek


def gen_vet(minwords, maxwords):
    vysledek = ""
    for i in range(randint(minwords, maxwords)):
        vysledek = vysledek + gen_slov() + " "
    return vysledek + "."



def menu():

    print("""Co chcete provést?
 1) Převod všech písmen na malá písmena.
 2) Nahrazení zanků jiným znakem.
 3) Generovat náhodný text.
 4) Statistika znaků
    """)
    volba = input("Zadejte číslo pro výběr operace: ")
    return volba


if __name__ == "__main__":
    volba = menu()


if volba == "3":    
    try:
         f2=open(input("Zadejte název výstupního souboru:"),"w")
    except FileNotFoundError:
        print("Soubor nenalezen!")    
    gen_slov()
    ps = int(input("Zadejte počet slov ve větě:"))
    gen_vet(ps,ps)
    veta = gen_vet(ps,ps)
    f2.write(veta)
elif volba == "1":
    mala()
elif volba=="4":
    stat()
elif volba == "2":
    znaky()
else:
    print("Nevhodný výběr.")

    
#Dal bych si 2 nebo 3, protože jsem na to dělal celé dvě odpoledne, funguje to, ale potřeboval jsem od Vás pomoc.