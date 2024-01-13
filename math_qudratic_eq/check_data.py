import math
import pyinputplus as pyinp
import time
from ask_for_eq import podanie_Parametrow,zapytaj

#pierwszy to wzór jaki ma funkcja
#drugi to numer wzoru

def podaj_parametry():
    wzor,numer  = podanie_Parametrow(zapytaj())

    prompt = f"""
    przyklad zmiennych jeśli wzór wygląda nieco inaczej i niema jedej z liczb to znaczy że trzeba wstawić 0
    1 kanoniczna np   -2(x-3)^2+5 --> gdzie a = -2 p = 3  q = -5 p,q =(x,y)wierzchołka
    2 ogólna         -3x^2 -5x -7 -->gdzie a = -3 b = -5x c = -7
    3  iloczynowa    -3(x+3)(x-10)--> gdzie a = -3 x1 = -3 x2 = 10 gdzie x1,x2= miejsca zaerowe \n"""
    print(prompt)
    zmienne = {}
    for i in wzor:

        zmienne[i] =(pyinp.inputFloat(f"podaj {i}: "))
    return zmienne,numer
#print(podaj_parametry())

def wzory(podaj_parametry):
    wzor,number = podaj_parametry   #wzór zwraca wzór czyli a,b,c i wartosci a numer to liczba1-3 i nazwa funkcji
    odzielnik = number[0]
    if odzielnik == "1":
       d =int( wzor["a"])
       e =int( wzor["p"])
       f =int( wzor["q"])
       a = d
       b = (-2*(e*d))
       c = ((e**2)*d)+f
       return a,b,c
    ## policzona jest git
    # a(x-x1)(x+x2) = a*(x^2-x+2x-2)
    elif odzielnik == "3":
        d =int( wzor["a"])
        e =int( wzor["x1"])
        f =int( wzor["x2"])
        a = d
        b= d *(-e-f)
        c = d*(-e)*(-f)
        return a,b,c

    a =int( wzor["a"])
    b =int( wzor["b"])
    c =int( wzor["c"])
    return a,b,c

#print(wzory(podaj_parametry()))
def user_input(user_input):
    flag = None
    user_input = user_input.lower()
    if user_input == "yes":
        flag  =True
        return flag
    elif user_input =="no" :
        flag  = False
        return flag
    if user_input != "yes" and user_input!="no":
        raise Exception ("PROSZE WPISAĆ POPRAWNIE yes/no bez zwracania uwagi na wielkość liter!!")



