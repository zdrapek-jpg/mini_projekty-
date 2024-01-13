import pyinputplus as pyinp

#wyświetlenie zapytania
def zapytaj():
    options  = ["1","2","3"]
    names = ["kanoniczna","ogólna","iloczynowa"]

    prompt = f"""
    wybierz format danych :
    1 kanoniczna np   -2(x-3)^2+5 --> gdzie a = -2 p = 3  q = -5 p,q =(x,y)wierzchołka
    2 ogólna 2x+5 lub -3x^2 -5x -7 -->gdzie a = -3 b = -5x c = -7
    3  iloczynowa    -3(x+3)(x-10)--> gdzie a = -3 x1 = -3 x2 = 10 gdzie x1,x2= miejsca zaerowe \n"""

    zapytanie =  pyinp.inputMenu(options,prompt,lettered = True)
    return zapytanie,names[int(zapytanie)-1]

#zdefiniowanie zapytania:

#funkcja decydująca o wyglądzie funkcji kwadratowej
def podanie_Parametrow(zapytanie):
    if zapytanie[0] == "1":
            return  ["a","p","q"],zapytanie

    elif zapytanie[0] == "2":
            return ["a","b","c"],zapytanie

    return ["a","x1","x2"],zapytanie
#print(podanie_Parametrow(zapytaj()))


