import time
import pprint
from random import *
import shelve
capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Francja': 'Paryż',
    'Wielka Brytania': 'Londyn',
    'Włochy': 'Rzym',
    'Hiszpania': 'Madryt',
    'Portugalia': 'Lizbona',
    'Holandia': 'Amsterdam',
    'Belgia': 'Bruksela',
    'Szwajcaria': 'Berno',
    'Austria': 'Wiedeń',
    'Czechy': 'Praga',
    'Słowacja': 'Bratysława',
    'Węgry': 'Budapeszt',
    'Chorwacja': 'Zagrzeb',
    'Słowenia': 'Lublana',
    'Serbia': 'Belgrad',
    'Czarnogóra': 'Podgorica',
    'Bośnia i Hercegowina': 'Sarajewo',
    'Macedonia Północna': 'Skopje',
    'Albania': 'Tirana',
    'Grecja': 'Ateny',
    'Turcja': 'Ankara',
    'Cypr': 'Nikozja',
    'Rosja': 'Moskwa',
    'Ukraina': 'Kijów',
    'Białoruś': 'Mińsk',
    'Litwa': 'Wilno',
    'Łotwa': 'Ryga',
    'Estonia': 'Tallin',
    'Szwecja': 'Sztokholm',
    'Norwegia': 'Oslo',
    'Dania': 'Kopenhaga',
    'Finlandia': 'Helsinki',
    'Islandia': 'Reykjavik',
    'Irlandia': 'Dublin',
    'Szkocja': 'Edynburg',
    'Walia': 'Cardiff',
    'Niemcy': 'Berlin',
    'Francja': 'Paryż',
    'Wielka Brytania': 'Londyn',
    'Włochy': 'Rzym',
    'Hiszpania': 'Madryt',
    'Portugalia': 'Lizbona',
    'Holandia': 'Amsterdam',
    'Belgia': 'Bruksela',
    'Szwajcaria': 'Berno',
    'Austria': 'Wiedeń',
    'Czechy': 'Praga'
}
## pętla głóna generująca pytania do quizu  i dodająca 3 losowe pytania i jedna poprawną 
for quiz_num in range(2):

    string = 'quiz_file'+str(quiz_num)
    file_quiz = open(f"{string}.txt","w")
    file_answers = open(f"{string}answers.txt",'w')
    file_quiz.write("sprawdzian z geografi\n     ")
    file_quiz.write(f"{' '*15}stolice państw test {quiz_num }")
    file_quiz.write("\n\n\n")   

    #losowanie odbywa się za pomocą metody shuffle  lista układa państwa losowo
    panstwa = list(capitals.keys())
    shuffle(panstwa)
    
    for question_number in range(5):
        
        correctAnswer = capitals[panstwa[question_number]]
        wrongAnswer =list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrong_3_Answers=sample(wrongAnswer,4)
        answers_quiz =  [correctAnswer]+wrong_3_Answers
        shuffle(answers_quiz)
        print(answers_quiz)
    #zapis pytania i odpowiedzi do pliku 

        file_quiz.write(f"Co jest stolicą {panstwa[question_number]} \n" ) 

        for i in range(5):
            file_quiz.write(f"{' '*6} {'ABCDE'[i]}.{answers_quiz[i]}")
            file_quiz.write("\n")
        file_answers.write(f"{question_number+1}.{'ABCDE'[answers_quiz.index(correctAnswer)]}\n")
    file_quiz.close()
    file_answers.close()


    
    
    #odpowiedzi do quizu 




