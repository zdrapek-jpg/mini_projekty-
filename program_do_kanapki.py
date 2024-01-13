# Tutaj pisz swój kod, młody padawanie ;-)
import pyinputplus as pyinp
import time
import json

pieczywo = { "pszenny":"2.30","razowy":"2.10","biały":"1.80","na zakwasie":"2.50"}
miensa = { "kurczak":"6.50","wołowina":"8.00","indyk":"5.50","szynka":"3.50"}
sery = {"cheddar":"0.80","szwajcarski":"0.50","mocarella":"1.10"}
dodatki = {"musztarda":"2.10","sałata":"1.20","pomidor":"0.80","majonez":"1.10"}

pieczywko,mienso  = [(key) for key in pieczywo.keys() ] , [(key) for key in miensa.keys()]
dodatek = [(key) for key in dodatki.keys()]

def kanapka(pieczywko,mienso):
    prompt = "wybierz pieczywo:\n"
    kanapka =  pyinp.inputMenu(pieczywko,prompt,lettered=True), pyinp.inputMenu(mienso,numbered=True)
    print(kanapka)
    time.sleep(1)
    return kanapka


def ser(sery):
    serki  = [klucz for klucz in sery.keys()]

    czySer = pyinp.inputYesNo("czy chcesz ser? ",yesVal = "tak",noVal = "nie")
    if czySer.lower()=="tak"or czySer.lower()=="t":
        prompt = "sery do wyboru:\n"
        ser = pyinp.inputMenu(serki,prompt,numbered=True)
        print(ser)
    else:
        ser = None
    time.sleep(0.8)
    return ser


def dodawanieKanapka(dodatek):
    prompt = " "
    dodaj = pyinp.inputYesNo(f"czy chcesz skorzystać z: {' '.join(dodatek) }?tak/nie ",yesVal = "tak",noVal="nie")
    if dodaj.lower()=="tak"or dodaj.lower()=="t":
        prompt = "wybierz jaki chcesz dodatek: \n"
        dodatek = pyinp.inputMenu(dodatek,prompt,numbered=True)
        print(dodatek)
    else:
        dodatek = None
    time.sleep(0.8)
    return dodatek


def iloscKanapek():
    ilosc=  pyinp.inputInt("ile przygotować Ci kanapek ? ",min=1,default =1 )
    time.sleep(0.8)
    print(ilosc)
    return ilosc


def SumaParagon(a,b,c,d):
    a1,a2 = a[0],a[-1]
    end_list = a1,a2,b,c,d
    time.sleep(1)
    return list(end_list)



while True:
    end_list  = SumaParagon(kanapka(pieczywko,mienso),ser(sery),dodawanieKanapka(dodatek),iloscKanapek())
    bread,meat,chees,adds,size = end_list
    print(f"kanapka/i {size}: chleb {bread} , mięso  {meat} , ser {chees} , dodatki {adds}")


    def is_in_menu(bread,meat,chees,adds,size,pieczywo,miensa,sery,dodatki):
        kanapka = 0
        a = float(pieczywo[bread])
        b = float(miensa[meat])
        kanapka = a+b
        if chees!=None:
            c = float(sery[chees])
            kanapka+=c
        if adds!=None:
            d = float(dodatki[adds])
            kanapka+=d
        return kanapka*int(size)
    print(is_in_menu(bread,meat,chees,adds,size,pieczywo,miensa,sery,dodatki),end="\n\n")
    time.sleep(0.5)
    print(f"do zapłaty: {is_in_menu(bread,meat,chees,adds,size,pieczywo,miensa,sery,dodatki)}")
    print("*"*10)
    time.sleep(0.8)
    print("tworzenie kolejnej kanapki....")
    time.sleep(2)



