import time,sys,json
import pyinputplus as pyinp

class Sandwitch:
    #główne słowniki cen
    pieczywo = { "pszenny":"2.30","razowy":"2.10","biały":"1.80","na zakwasie":"2.50"}
    miensa = { "kurczak":"6.50","wołowina":"8.00","indyk":"5.50","szynka":"3.50"}
    sery = {"cheddar":"0.80","szwajcarski":"0.50","mocarella":"1.10"}
    dodatki = {"musztarda":"2.10","sałata":"1.20","pomidor":"0.80","majonez":"1.10"}
    ## tylko klucze programu 
    pieczywka_keys = [key for key in pieczywo.keys()]
    mienska_keys = [key for key in miensa.keys()]
    serki_keys = [key for key in sery.keys()]
    dodateczki_keys = [key for key in dodatki.keys()]

    #zmienna główna
    full_price = {}
    ## poglądowe wyświetlenie 
    def displayInformation(self):
        print(Sandwitch.pieczywka_keys)
        print(Sandwitch.mienska_keys)
        print(Sandwitch.serki_keys)
        print(Sandwitch.dodateczki_keys)

    #wyświetlenie pętli i menu wyboru  składników 
    def chooseBread(self):
        return  pyinp.inputMenu(Sandwitch.pieczywka_keys,"wybierz pieczywo na kanapkę:\n",default="biały",lettered=True)

    def chooseMeat(self):
        return  pyinp.inputMenu(Sandwitch.mienska_keys,"wybierz mięso:\n",numbered=True)

    def chooseChees(self):
        return  pyinp.inputMenu(Sandwitch.serki_keys,"wybierz ser jaki chcesz\n",numbered=True)
        
    ## dodatków może być nieskończenie dużo 
    def chooseAdditives(self):
        list_Additives = []
        flag = True
        list_Additives.append(pyinp.inputMenu(Sandwitch.dodateczki_keys,"co chcesz dodać:\n",numbered=True))
        while flag:
            #skończenie wykonania
            flag  =self.inputFlag("dodać jeszcze jakieś dodatki?")
            if flag == False:
                break
            list_Additives.append(pyinp.inputMenu(Sandwitch.dodateczki_keys,"co chcesz jeszcze dodać:\n",numbered=True))


        return list_Additives
        
    ## logika każdej pętli kontynuacji 
    def inputFlag(self,text):
        flag = pyinp.inputYesNo(prompt=text,yesVal="yes",noVal="no")
        #sprawdzenie logiki i zwrucenie boola
        return True if (flag.lower()  == "y" or flag.lower() == "yes") else False 
    
    # nadpisanie pliku tekstem
    def WriteRecipe(self,text_to_write):
        with open(r"Program_kanapka\paragon_kanapka.txt","a+",encoding="utf-8") as file_write:
            file_write.write(text_to_write+"\n")
            

    #wyciągnięcie cen za konkretne rzeczy 
    def getPrices(self,bread_taken,meat_taken,cheese_taken,additives_taken,cena):
        # new dictonary for json file
        paragon,full_price = {},{}
        #liczenie ceny i display na konsoli co za ile
        cena += float(self.pieczywo[bread_taken])   
        self.WriteRecipe(f"chleb {bread_taken: ^15}:{self.pieczywo[bread_taken]:>5} zł")
        paragon['pieczywo']= bread_taken

        if meat_taken!= "":
            cena += float(self.miensa[meat_taken])
            self.WriteRecipe(f"mięso {meat_taken:^15}:{self.miensa[meat_taken]:>5} zł")
            paragon["mięso"]= meat_taken

        if cheese_taken!="":
            cena+= float(self.sery[cheese_taken])
            self.WriteRecipe(f"ser {cheese_taken:^15}:{self.sery[cheese_taken]:>5} zł" )
            paragon['ser'] = cheese_taken

        if additives_taken!= "":
            self.WriteRecipe(f"dodatki :")

            if len(additives_taken)==1:
                cena+= float(self.dodatki[additives_taken[0]])
                self.WriteRecipe(f"--- {additives_taken[0]:^15}:{self.dodatki[additives_taken[0]]:>10} zł")
                paragon['additives'] = additives_taken

            elif len(additives_taken)>1:
                additives_paragon= []
                for add in additives_taken:
                    cena+= float(self.dodatki[add])
                    self.WriteRecipe(f"--- {additives_taken[0]:^10}:{self.dodatki[additives_taken[0]]:>10} zł")
                    additives_paragon.append(add)
                paragon['additives']=additives_paragon
        paragon['price']=cena
        return (cena,paragon)
    
    # last  na false nie sumuje cen tylko zapisuje słownik  kiedy jest na true zapisuje cene finałową 
    def update_json_price(self,price,last,paragon=""):
        if last:
            Sandwitch.full_price['price_full']=price
            with open(r"Program_kanapka/kanapka_order.json","w",encoding="utf-8") as json_file:
                json.dump(Sandwitch.full_price,fp = json_file)
                json_file.close()

        elif not(last):
            with open(r"Program_kanapka/kanapka_order.json","w",encoding="utf-8") as json_file:
                json.dump(paragon,fp = json_file,ensure_ascii=False,indent=4)
                json_file.close()
            



   
        
        
        
       
        
    
       
   
    
    






