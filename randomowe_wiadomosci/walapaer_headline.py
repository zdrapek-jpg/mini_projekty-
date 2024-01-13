# Tutaj pisz swój kod, młody padawanie ;-)
import random

Person = ["He", "She" ,"It","They"]
POSSESIVE_PRONOUNS = ['Her', 'Him', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']

STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
    'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
    'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
    'Plastic Straw','Serial Killer', 'Telephone Psychic']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
    'Workplace', 'Donut Shop', 'Apocalypse Bunker']

BEFORE= ['Soon', 'This Year', 'RIGHT NOW',"At Least"]
AFTER= ['Later Today','Next Week', "Next Year", "In Future"]
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
def main ():
    head_Line=[]
    while True:
        ilosc = input("ile chcesz stworzyć tytułów? ")
        if not ilosc.isdecimal():
            print('Prosze podac liczbe.')
        else:
            break
    for i in range(int(ilosc)):
        clickbaitType = random.randint(1, 6)
        if clickbaitType == 1:
            headline = opcja1()
        elif clickbaitType == 2:
            headline = opcja2()
        elif clickbaitType == 3:
            headline = opcja3()
        elif clickbaitType == 4:
            headline = opcja4()
        elif clickbaitType == 5:
            headline = opcja5()
        elif clickbaitType==6:
            headline = opcja6()
        head_Line.append(headline)
    return head_Line




def opcja1():
    return f"The {random.choice(PLACES)} that was robbed {random.choice(BEFORE)}"

def opcja2():
    return f" The {random.choice(STATES)} is the first one to change law {random.choice(AFTER)}"

# KaĪda z tych funkcji zwraca róĪny rodzaj nagáówka:
def opcja3():
    return f'Are Millenials Killing the {random.choice(AFTER)} Industry?'

def opcja4():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun,when)

def opcja5():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}'

def opcja6():
    return f"Goha Goha 2 zł in {random.choice(PLACES)} , Tour For {random.choice(AFTER)}!"

them = main()
for it in them: print(it)




def Collatz_Problem():
    while True:
        number = input("podaj liczbę większą od zera : ")
        if not  number.isdecimal():
            number  =input("muspisz podać liczbę (dodatnią: ")
        if number.isdecimal():
            break
    number =int(number)
    while number!=1 and number!=0:
        if number %2 ==0:
            number/=2
        elif number %2!=0:
            number = number*3+1
        elif number==1:
            priny("1")
        print(number)
print(Collatz_Problem())



