import pyinputplus as pyinp
from random import randint,choice
import time

flag_play = True
score   = 0
question_answer=[]
emoji_good = ["😎","🥳","😄","🤪",]
emojis_bad = ["😢","😭","😖"]

def dodawanie(num1,num2):
    lista = (f"wyrażenie {num1}+{num2} jest równe : ",num1+num2)
    return lista


def odejmowanie(num1,num2):
    lista = (f"wyrażenie {num1}-{num2} jest równe : ",num1-num2)
    return lista

def multiply(num1,num2):
    lista = (f"wyrażenie {num1}*{num2} jest równe : ",num1*num2)
    return lista

while flag_play==True:
    
    question_answer.append(dodawanie(randint(-10,40),randint(10,40)))
    question_answer.append(odejmowanie(randint(1,50),randint(1,50)))
    question_answer.append(multiply(randint(-5,9),randint(-3,11)))
    quiz = choice(question_answer)

    try :
        if flag_play==False:
            break
        player = pyinp.inputStr(f"{quiz[0]}",allowRegexes = [str(quiz[-1])],blockRegexes =['.*',"źle"],timeout=12,limit=3)
        if player== str(quiz[-1]):
            print(f"dobra odpowiedź{choice(emoji_good)}")
            score+=1
        question_answer.clear()
        continue_game = pyinp.inputYesNo("czy chcesz kontynuować y/n? ")
        if continue_game.lower()=="no" or  continue_game.lower()=="n" :
            flag_play=False
            
    except pyinp.TimeoutException:
        print(f"czas miną! {choice(emojis_bad)}")
        continue_game = pyinp.inputYesNo("czy chcesz kontynuować y/n? ")
        if continue_game.lower()=="no" or  continue_game.lower()=="n" :
            flag_play=False
        continue
        
    except pyinp.RetryLimitException:
        print(f"zbyt wiele prób! {choice(emojis_bad)}")
        continue_game = pyinp.inputYesNo("czy chcesz kontynuować y/n? ")
        if continue_game.lower()=="no"or  continue_game.lower()=="n":
            flag_play=False
        continue

prompt= "Wynik końcowy to "
print(f"{prompt} : {score}")
