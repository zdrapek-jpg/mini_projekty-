#! python3
#mclip.py --program dla schowka

import sys,pyperclip
text = {"zgoda":"Tak zgadzam się",
        "odmowa":"nie nie zgadzam sie na to ",
        "zapytanie":"czy możemy to przełożyć na następny tydzień??"}

if len(sys.argv)<2:
    print('użycie : pythona [skrut] skopiowanie wskazanej wiadomości')
    sys.exit()
keyphrase= sys.argv[1]
if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"wiadomość o treści {text[keyphrase]} została skopiowana do schowka")
else:
    print(f"nie instniej wiadomość dla {keyphrase}")
