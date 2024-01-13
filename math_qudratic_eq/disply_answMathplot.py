import time
import math
import pyinputplus as pyinp
from check_data import wzory, podaj_parametry,user_input
import sys
import numpy as np
import random
from matplotlib import pyplot as plt


def liczenie(wzory):
    a,b,c = wzory
    if a == 0 :
        try:
            x0 = (-c)/b
            m = b>0
            if m == True:
                return f"{b}x+{c} rosnąca x0 = {x0}"
            return f"{b}x+{c} malejąca x0 = {x0}"
        except:
            return f"funkcja stała {c}"

    delta  = (b**2) -(4*a*c)
    zmienne = []
    try:
        if delta <0:
            print (f"{a}x^2+{b}x+{c} i brak miejsc zerowych ")
            zmienne.append(a)
            zmienne.append(b)
            zmienne.append(c)
            return zmienne

        elif delta == 0:
            x0 = (-b)/(2*a)
            zmienne = a,b,c,round(x0,2)
            print (f"{a}x^2+{b}x+{c} i 1 miejsce zerowe {round(x0,4)} {sqrt_delta}")
            return zmienne
        elif delta >0:
            sqrt_delta = math.sqrt(delta)
            sqrt_delta= round(sqrt_delta,4)
            x1 =round((-b-sqrt_delta)/2*a,4)
            x2 =round((-b+sqrt_delta)/2*a,4)
        print ( f"{a}x^2+{b}x+{c} i 2 miejsca zerowe  pierwiastek z delty:{sqrt_delta} x1={x1},x2={x2}")
        zmienne = a,b,c,x1,x2
        return zmienne
    except:
        return "coś poszło nie tak  za chwilę program sie sam zamknie :)"
        time.sleep(5)
        sys.exit()

X =[]
Y = []




flag  = True
while flag  == True:

    zmienne =(liczenie(wzory(podaj_parametry())))
    print(zmienne)
    print("wpisz yes(kontynuj)/no(zakończ) :",end= " ")

    flag= pyinp.inputCustom(user_input)
    if flag ==False:
        time.sleep(3)
        sys.exit()


