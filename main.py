#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:8.11.2021
# Autor:Dominik Šlehofer
############################################################################
from random import randint, choice

############################################################################


def menu():
    print("""Co chcete provést?
1) Převod všech písmen na malá písmena.
2) Nahrazení zanků jiným znakem.    
3) Generovat náhodný text.
""")
    volba = input("Zadejte číslo pro výběr operace: ")
    return volba


if __name__ == "__main__":
    volba = menu()


try:
    f1=open(input("Zadejte název vstupního souboru:"),"r")
except FileNotFoundError:
    print("Soubor nenalezen!")


f2=open(input("Zadejte nazev výstupního souboru:"), "w")



#generovaní textu s volbou počtu slov
samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"
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


ps = int(input("Zadejte počet slov ve větě:"))

def gen_vet(minwords=ps, maxwords=ps):
    vysledek = ""
    for i in range(randint(minwords, maxwords)):
        vysledek = vysledek + gen_slov() + " "
    return vysledek + "."

veta = gen_vet()

if volba == "3":
    f2.write(veta)




#převod písmen na malá písmena 
def mala():
    text = f1.read().lower()
    f2.write(text)

if volba == "1":
    mala()


#převod určitého znaku na jiný znak
while volba == "2":
    znak = f1.read(1)
    if znak == "": 
        break
    if znak == "A":
        znak = "&"
    f2.write(znak)



f1.close()
f2.close()
    
