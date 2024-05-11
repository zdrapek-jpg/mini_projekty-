# Tutaj pisz swój kod, młody padawanie ;-
from random import randint
import pyinputplus as pyinp
# olej z czarnuszki na włosy na głwoie  podobno bardzo dobry
zgadniete =0
low = [1,10,5]
medium=[1,20,6]
high = [1,100,7]
wybur = [low,medium,high]
game = True

while game == True:
    start=True

    print(f"""podaj poziom na jakim chcesz grać:
    [początek,koniec,ilość szans]
    1     {low}
    2    {medium}
    3     {high} """)
    while True:
        choice = pyinp.inputNum("wybierz poziom 1,2 lub 3 ",min=1,max=3)
        if choice== 1 or choice== 2 or choice== 3:
            break
    opcja = wybur[choice-1]
    print(f" wybrałeś opcje start: {opcja[0]}  stop: {opcja[1]} ilość szans: {opcja[2]}")
    while start==True:
            #wylosoanie liczby którą zgadujemy
            liczba_do_zgadniecia = randint(opcja[0],opcja[1])

            print("wpisz zgadywaną liczbę jeśli nie trafisz to Ci podpowiem :")

            for  i in range(1,opcja[2]+1):
                user_input = pyinp.inputNum(" ")
                if user_input == liczba_do_zgadniecia:
                    print(f"gratulacje wylosowałem {liczba_do_zgadniecia} a ty trafiłeś/aś")
                    zgadniete+=1
                    break
                if user_input<liczba_do_zgadniecia:
                    print(f"liczba jest za mała zgaduj dalej, szanse: {opcja[2]-i}")
                if user_input>liczba_do_zgadniecia:
                    print(f"liczba jest za duża  zgaduj dalej, szanse: {opcja[2]-i}")

            start= False
    x=input(" grasz jeszcze raz :y/n?")
    if x.lower()== "n":
        break

print(f"twój wynik: {zgadniete}  win jak na Ciebie dobry wynik ;p ")
