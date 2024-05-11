#!Python3
# program napisany w tkinter z modułęm ttkbootstrap który imituje gre w papier kamień norzyce
import json, sys
from random import choice
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class App(tk.Tk):
    path = r"C:/Users/Acer/mu_code/mini_projekty/papier_kamien/dane_gry.json"
    points = {}
    def __init__(self):
        #setup
        super().__init__()
        self.title('Gra kulko kzyz')
        self.geometry("570x450")
        self.minsize(400,300)

        #create widget
        self.top = Menu(self)
        #center buttons
        self.center = Przyciski(self)
        self.Score_Label = ttk.Label(self,text="".center(20),font=16, background='lavender blush',foreground='black')
        self.Score_Label.pack(padx=5,pady=5,side='top')
        self.Score = ttk.Label(self,text = " ".center(20),font=18, background='lavender blush',foreground='blue')
        self.Score.pack(padx=5,pady=5)
        ttk.Button(self,text="Reset Score",command=lambda: reset_stats(self)).pack(padx=5,pady=10,side='left')
        ttk.Button(self,text="exit",width=15,command=lambda: sys.exit()).pack(padx=5,pady=10,side='left')

        #run app
        self.mainloop()



class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        ttk.Label(self,text="witaj w grze papier, kamień, nożyce ",foreground='blue',background='PaleTurquoise2',font=20).pack()
        ## zbudowanie Framu
        self.pack(pady=5)
class Przyciski(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.game_view =ttk.Label(self,text="zacznij grać",font=18,foreground='blue4',background='PaleTurquoise3')
        self.game_view.pack(padx=20,pady=30)
        ttk.Button(self, text='Scissors',width=12,command=lambda:player_take('scissors',self)).pack(padx=10,pady=20,side='left')
        ttk.Button(self,text="Paper",width=12,command=lambda:player_take('paper',self)).pack(padx=10,side='left')
        ttk.Button(self,text='Rock',width=12,command=lambda:player_take('rock',self)).pack(padx=10,pady=20,side='left')
        ## self config of frame
        self.configure(width=360,height=280,border=3,borderwidth=20,relief=tk.GROOVE,padding=20,)
        self.pack()

def player_take(arg,instance):
    Player = arg
    Ai_choice = choice(['rock','scissors','paper'])
    global player_win
    player_win= "Win" if (Player=='rock' and Ai_choice=='scissors' )or (Player=='scissors' and Ai_choice=='paper')or (Player=='paper' and Ai_choice=='rock') else "Loose" if (Player=='rock' and Ai_choice=='paper' )or (Player=='scissors' and Ai_choice=='rock')or (Player=='paper' and Ai_choice=='scissors') else "Draw"
    instance.game_view.configure(text=f"{Player} vs {Ai_choice} {player_win}")
    take_and_write_score(instance.master)

def take_and_write_score(instance_master):
    try :
            with open(App.path,"rb") as file_read:
                App.points = json.load(file_read)
                points = App.points
    except :
            with open("dane_gry.json","w")as create_file:
                points = {"Win":0,"Loose":0,"Draw":0}
                json.dump(points,create_file,indent=4)
                App.points = points
                points =App.points

    if player_win == "Win":
        instance_master.Score_Label.configure(text=f"WYGRYWASZ!😊")
        points['Win']+=1

    if player_win == "Loose":
       instance_master.Score_Label.configure(text=f"PRZEGRYWASZ..😔")
       points['Loose']+=1

    if player_win== "Draw":
        instance_master.Score_Label.configure(text="REMISS😐")
        points['Draw']+=1

    instance_master.Score.configure(text = " wygrane {} przegrane{} remisy {}".format(points['Win'],points['Loose'],points['Draw']))
    with open(App.path, 'w') as fp:
        json.dump(points, fp)
        fp.close()
def reset_stats(master):
    with open(App.path, 'w') as fp:
        json.dump({"Win":0,"Loose":0,"Draw":0}, fp)
        fp.close()
    points ={"Win":0,"Loose":0,"Draw":0}
    master.Score.configure(text = " wygrane {} przegrane{} remisy {}".format(points['Win'],points['Loose'],points['Draw']))

window = App()
