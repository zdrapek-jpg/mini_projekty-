# Tutaj pisz swój kod, młody padawanie ;-)
import time, sys


def zygzaczek(wciencie,pattern,ilosc):
    przesuwanie= True
    try:
        while True:
            print(" " * wciencie,end="")
            print(pattern*ilosc)
            time.sleep(0.2)
            if przesuwanie:
                wciencie+=1
                if wciencie==30:
                    przesuwanie=False
            else:
                wciencie-=1
                if wciencie==0:
                    przesuwanie=True
    except KeyboardInterrupt:
        sys.exit()
#print(zygzaczek(int(input("podaj wciencie od którego zaczniesz ")),input("podaj znak : "),int(input("podaj ilość znaków"))))

#################program choinka
wiadomosc  = "choinka"

print(wiadomosc.center(30,"*").upper())

wysokosc =int(input("podaj wysokość"))
budulec = input("z czego to zbudowac?")
spacje = wysokosc+5
gwiazdki = 1

for  i in range(0,wysokosc):
    print(" "*spacje,end=" ")
    print(budulec*gwiazdki)
    spacje-=1
    gwiazdki+=2
stojak = gwiazdki//20
for  i in range(3):
    print(" " *( wysokosc+4), end= " ")
    print("%"*stojak)


#zadanie zaliczeniowe
def collatz (number):
    while number >=1:
        if number%2 == 0:
            number = number//2
            print(number)
        elif number%2==1:
            number = (3*number)+1
            print(number)
        if number == 1:
            print(number)
            break
x= True
while x== True:
    try:
        number = int(input("podaj liczbę : "))
        print(collatz(number))
        x= False

    except ValueError:
        print("niewłaściwie podana wartość")

#exclusive przypisanie  idexu i wartosći pod indexem
dni_tygodnia = ["p","w","s","cz","p","s","n"]
Poniedzialek,wtorek,sroda,czwartek,piontke,sobota,niedziela= dni_tygodnia
print(wtorek)
for index,item in enumerate(dni_tygodnia):
    print(index,item)
#modyfikuje liste nie zmienijąc jej zmieinia kolejności losowo
#metoda shuffle(lista)
string = ''
wyjdz = True
while wyjdz ==True:
    doloncz = input("podaj text który chcesz dołączyć: ")
    string+= " "+doloncz
    print(string)
