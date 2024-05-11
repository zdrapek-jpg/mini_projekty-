from kanapka import Sandwitch 
import json
import smtplib
import ssl
from email.message import EmailMessage
import re 
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import sys


def mail_sender(recipe):
    #wczytanie informacji 
    with open(r"Program_kanapka/email.json",'r')as email_configuration:
        mail_holder = json.load(email_configuration)
    # obiekt z konta servera  smtp 
    sender_email = mail_holder['sender_email']
    password = mail_holder['password']   ### KUUUUUURWAAAAAAAAA
    receiver_email = mail_holder['receiver_email']
    subject = "wiadomość"
    body = f"\n  {recipe} "
    em = EmailMessage()
    em['From']=sender_email
    em['To'] = receiver_email
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login(sender_email,'chip dnwx grdh ozxq')
        server.send_message(em)


flag,i = True,1
prices = []
while flag :
    price = 0

    ## obiekt do obsługi metod 
    key = Sandwitch()
    #wywołanie wszystkich metod wyboru składników 
    #zapytanie czy chemy poszczegulny rzeczy 
    bread_take = key.chooseBread()

    take_meat = key.inputFlag("czy chcesz dodać mięso?:y/n")
    meat_take = key.chooseMeat() if take_meat else ""

    take_chees = key.inputFlag("czy chcesz dodać ser?:y/n")
    cheese_take = key.chooseChees() if take_chees else ""

    take_additives = key.inputFlag("czy chcesz dodatki?:y/n")
    additives_taken= key.chooseAdditives() if take_additives else ""
   
    #wywołanie wyboru wszystkiego z powyżej i pprzepisanie do pliku  do zapisu w pliku 
    #dodajemy do ceny końcowej która będzie wy świetlona po zakończeniu pętli programu 
    price_for_sandwitch,el2 =  key.getPrices(bread_take,meat_take,cheese_take,additives_taken,price)
    # cena łączna 
    price  +=price_for_sandwitch
    prices.append(price)

    # słownik do zapisu  w pliku json
    key.update_json_price(price,False,el2)
    
    #zapytanie czy kontynuować
    flag = key.inputFlag("czy chcesz zrobić kolejną kanapkę?:y/n")
    i+=1

    key.WriteRecipe(f"Price {price:>10}   zł\n")  

key.WriteRecipe(f"Total Price {sum(prices):>10} zł")  

#odczyt pliku
with open(r"Program_kanapka\paragon_kanapka.txt","r",encoding="utf-8") as file_writen:
    file_paragon  = file_writen.read()

#       wysłanie maila
mail_sender(file_paragon)
print("mail sent")
