# Tutaj pisz swój kod, młody padawanie ;-)
from random import randint
import json
import pyinputplus as pyinp
game_score = []
welcome =  " witaj w grze papier, kamień, nożyce "
print(welcome.center(50,"#").upper())
path_file = 'C:/Users/Acer/mu_code/mini_projekty/dane_gry.json'
i =0
with open(path_file,"rb") as reading:
    game_score=json.load(reading)

print(f" wygrane: {game_score[0]} remisy : {game_score[1]} przegrane : {game_score[2]}")


wynik = []
choice = True
take = ["paper","scissors","rock"]

while choice==True:
    player_choice =pyinp.inputMenu(["paper","scissors","rock"],numbered=True)
    AI_choice = take[randint(0,2)]

    print(f"walka : {player_choice } vs {AI_choice}")

    if player_choice==AI_choice:
        print("remis")
        game_score[1]+=1
    if player_choice=="scissors" and AI_choice=="rock":
        print("PRZEGRYWASZ..")
        game_score[2]+=1
    if player_choice=="scissors" and AI_choice=="paper":
        print("WYGRYWASZ")
        game_score[0]+=1
    if player_choice=="paper" and AI_choice=="rock":
        print("WYGRYWASZ")
        game_score[0]+=1
    if player_choice=="paper" and AI_choice=="scissors":
        print("PRZEGRYWASZ..")
        game_score[2]+=1
    if player_choice=="rock" and AI_choice=="scissors":
        print("WYGRYWASZ")
        game_score[0]+=1
    if player_choice=="rock" and AI_choice=="paper":
        print("PRZEGRYWASZ..")
        game_score[2]+=1

    print(f"wynik rozgrywki to : wygrane: {game_score[0]}, remisy: {game_score[1]}, przegrane: {game_score[2]} ")
    clear_game_score= pyinp.inputYesNo("czy chcesz zrestartować wynik gry?",yesVal = "tak",noVal="nie",blank=True)
    if clear_game_score=="nie " or clear_game_score=="n":
        game_score=[0,0,0]
    end = pyinp.inputYesNo("czy chcesz kontynuować grę (t)ak/(n)ie?",yesVal = "tak",noVal="nie",blank=True)
    if  end.lower() == "nie" or end.lower()=="n" :
        choice = False

with open(path_file,"w")as fp:
        json.dump(game_score,fp)
        fp.close()






