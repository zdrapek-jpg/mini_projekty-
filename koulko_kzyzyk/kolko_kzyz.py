# Tutaj pisz swój kod, młody padawanie ;-)
#gra kułko krzyżyk
Board = {
    "1":"","2":"","3":"",
    "4":"","5":"","6":"",
    "7":"","8":"","9":""
}


#wyświtelenie jak planszy
def printing(Board):
    print(f"{Board['1']} | {Board['2']} | {Board['3']}")
    print("--+---+--")
    print(f"{Board['4']} | {Board['5']} | {Board['6']}")
    print("--+---+--")
    print(f"{Board['7']} | {Board['8']} | {Board['9']}")
Tura_gracza = " "
while not (Tura_gracza == 'X' or Tura_gracza == 'O'):
    print('Do you want to be X or O?')
    Tura_gracza = input().upper()

#pętla gry główna 9 znaków
for i in range(9):
    print(printing(Board))

    one = Board["1"] == Board["2"] == Board["3"] == "X"
    two = Board["4"] == Board["5"] == Board["6"] == "X"
    tree = Board["7"] == Board["8"] == Board["9"] == "X"
    four = Board["1"] == Board["4"] == Board["7"] == "X"
    five = Board["2"] == Board["5"] == Board["8"] == "X"
    six = Board["3"] == Board["6"] == Board["9"] == "X"
    seven = Board["1"] == Board["5"] == Board["9"] == "X"
    eight = Board["3"] == Board["5"] == Board["7"] == "X"

    has_X_line = one or two or tree or four or five or six or seven or eight
    if has_X_line:
        print("wygrana X")
        take=False
        break

    one = Board["1"] == Board["2"] == Board["3"] == "O"
    two = Board["4"] == Board["5"] == Board["6"] == "O"
    tree = Board["7"] == Board["8"] == Board["9"] == "O"
    four = Board["1"] == Board["4"] == Board["7"] == "O"
    five = Board["2"] == Board["5"] == Board["8"] == "O"
    six = Board["3"] == Board["6"] == Board["9"] == "O"
    seven = Board["1"] == Board["5"] == Board["9"] == "O"
    eight = Board["3"] == Board["5"] == Board["7"] == "O"

    has_O_line = one or two or tree or four or five or six or seven or eight
    if has_O_line:
        print("wygrana DZIURKA XD ")
        take=False
        break
    move = input(f"""podajesz  miejsce w którym chcesz wstawić znak {Tura_gracza} przykład:
    1 | 2 | 3
    --+---+--
    4 | 5 | 6
    --+---+--
    7 | 8 | 9
    """)
    take= True

    while take==True:
        if Board[move]== "X" or Board[move]=="O":
            move = input("podaj inne miejsce")
            if Board[move] ==" ":
                take =False
        Board[move] = Tura_gracza
        if Tura_gracza == "X":
            Tura_gracza = "O"
        else:
            Tura_gracza= "X"
        break


