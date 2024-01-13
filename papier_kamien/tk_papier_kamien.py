# Tutaj pisz swój kod, młody padawanie ;-)
from tkinter import Tk as tk
from tkinter import Label
from tkinter import Button
from random import randint
import json
root = tk()
path_file = 'C:/Users/Acer/mu_code/mini_projekty/dane_gry.json'

welcome =  (" witaj w grze papier, kamień, nożyce ".center(50,"*").upper())
wynik = []
choice = True
take = ["paper","scissors","rock"]

with open(path_file,"rb") as reading:
    game_score=json.load(reading)
root["background"]='#856ff8'


root.title("Firts App")
root.geometry("700x600")

label = Label(root,bg='#856ff8', text=welcome, font=20, fg="red")
label.pack()

text_label = Label(root,bg='#856ff8', text="zacznij grać", font=30, )
text_label.pack()



def play(player_choice,AI_choice):
    global score_game
    if player_choice==AI_choice:
        game_score[1]+=1
        return None
    if player_choice=="scissors" and AI_choice=="rock":
        game_score[2]+=1
        return True
    if player_choice=="scissors" and AI_choice=="paper":
        game_score[0]+=1
        return True
    if player_choice=="paper" and AI_choice=="rock":
        game_score[0]+=1
        return True
    if player_choice=="paper" and AI_choice=="scissors":
        game_score[2]+=1
        return False
    if player_choice=="rock" and AI_choice=="scissors":
        game_score[0]+=1
        return True
    if player_choice=="rock" and AI_choice=="paper":
        game_score[2]+=1
        return False
    print(game_score,1)

def play_begin(player_choice):
    global text_label
    AI_choice = take[randint(0,2)]
    is_user_winner = play(player_choice,AI_choice)
    if is_user_winner is None:
        text_label.config(text="REMISS😐",fg="blue")
        label.config(text=f"wynik rozgrywki to : wygrane {game_score[0]}, remisy {game_score[1]}, przegrane {game_score[2]}")
    if is_user_winner is True:
        text_label.config(text="WYGRYWASZ!😊",fg="green")
        label.config(text=f"wynik rozgrywki to : wygrane {game_score[0]}, remisy {game_score[1]}, przegrane {game_score[2]}")
    if is_user_winner is False:
        text_label.config(text="PRZEGRYWASZ..😔",fg="red")
        label.config(text=f"wynik rozgrywki to : wygrane {game_score[0]}, remisy {game_score[1]}, przegrane {game_score[2]}")



Button1=Button(root, text="papier", width=15,height=5,bg="orange",command=lambda:play_begin("paper"))
Button1.pack()
Button2=Button(root, text="kamien", width=15,height=5,bg="purple",command=lambda:play_begin("rock"))
Button2.pack()
Button3=Button(root, text="nożyce", width=15,height=5,bg="pink",command=lambda:play_begin("scissors"))
Button3.pack()

label = Label(root,bg='#856ff8', text=f"wynik rozgrywki to : wygrane {game_score[0]}, remisy {game_score[1]}, przegrane {game_score[2]},", font=35, fg="red")
label.pack(side="bottom", pady=80,padx=20)

def save_game_score(game_score):
    with open(path_file, 'w') as fp:
        json.dump(game_score, fp)
        fp.close()

def exit_button_clicked(game_score):
    save_game_score(game_score)
    root.destroy()  # Zamyka okno Tkinter


# Tworzenie przycisku Exit
exit_button = Button(root, text="Exit",width=10,height=5, command=lambda: exit_button_clicked(game_score))
exit_button.pack()


root.mainloop()
