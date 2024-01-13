#! python3
#phone-email-data  : wyszukiwanie
import pyperclip
import time
import re

text = str(pyperclip.paste())
###telefon
regexPhone2 =re.compile(r"""
\s(\d{2})?
(\.|\-|\s)?
(\d{3})
(\.|\-|\s)?
(\d{2})
(\.|\-|\s)?
(\d{2})
(\.|\-|\s)?
(\d{2})?
""",re.VERBOSE)

regex_Phone= re.compile(r"""
(\(\d{2}\)|\d{2})?
(\.|\-|\s)?
(\d{3})
(\.|\-|\s)
(\d{3})
(\.|\-|\s)
(\d{3})
""",re.VERBOSE)


### mail
mailRegex = re.compile(r"""
([a-zA-Z0-9._!#$%&+-]+)
(@)
([a-zA-Z0-9._#$%&+-]+)
""",re.VERBOSE)

##### data poprawna dzień miesiąc lata 1910-2024   dd\.-mm\.-rrrr
correct_data = re.compile(r"""
(
(0[1-9]|[1-2][0-9]|30)                  #dni 1-30
(\.|\-|\/)                                # znaki między dzień miesiąc
(04|06|08|10|4|6|8)                        # miesiące które mają 30 dni max
(\.|\-|\/)                                   #  znaki między miesiąc rok
((19[1-9][0-9])|(20[0-1][1-9]|20[2][0-4]))     #lata od 1910-2024
)|
(
(0[1-9]|[1-2][0-9]|30|31)                #dni 1-31
(\.|\-|\/)                               # znaki między dzien miesiąć
(1|3|5|7|9|11|12|01|03|05|09|07)         # miesiące które mają do 31 dni w foramcie 0 cyfra miesiąca lub sama cyfra
(\.|\-|\/)                                # znaki między miesiąć rok
((19[1-9][0-9])|(20[0-1][1-9]|20[2][0-4]))  #rok w formacie 1910-2024
)||
(
(0[1-9]|[1-2][0-9])                #dni 1-29
(\.|\-|\/)                               # znaki między dzien miesiąć
(2|02)         # miesiąc luty
(\.|\-|\/)                                # znaki między miesiąć rok
((19[1-9][0-9])|(20[0-1][1-9]|20[2][0-4]))  #rok w formacie 1910-2024
)

""",re.VERBOSE)


#### data
regexData = re.compile(r"""
(\d{4}|0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])
(\.|\-|\\)
(0[1-9]|1[0-2]|[1-9])
(\.|\-)
(\d{4}|\d{2})
""",re.VERBOSE)
# łączenie krotek z dopasowaniami
dopasowania = []
for grupa in regexPhone2.findall(text):
    string = ""
    for element in grupa:
        string+=element
    dopasowania.append(string)
for grupa in regex_Phone.findall(text):
    string = ""
    for element in grupa:
        string+=element
    dopasowania.append(string)
for grupa in mailRegex.findall(text):
    string = ""
    for element in grupa:
        string+=element
    dopasowania.append(string)
for grupa in regexData.findall(text):
    string = ""
    for element in grupa:
        string+=element
    dopasowania.append(string)
#for data  in correct_data.findall(text):
#    if len(data[0])>4:
#        dopasowania.append(data[0])
#    if len(data[8])>5:
#        dopasowania.append(data[8])
#    if len(data[16])>5:
#        dopasowania.append(data[16])
#
print('znaleione dopasowania:')
print('-------------------')
time.sleep(1)
for  i in dopasowania:
    print(i.rjust(20,"*"))
    time.sleep(0.2)
    if len(dopasowania)<=0:
        print("nie znaleziono żadnych dopasowań daty/maila/telefonu")
time.sleep(100)

