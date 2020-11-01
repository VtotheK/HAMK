import perus
from os import name, system
def clearconsole():
    if(name == "nt"):
        system("cls")
    else:
        system("clear")

def greeting():
    print("""
|*******************************************************|
|               HAMK Perustehtäviä                      |
|*******************************************************|
|Paina haluaamasi numeronäppäintä valitatksesi ohjelman.|
|1.Hello world                                          |
|2.Yhteenlasku                                          |
|3.Luvun neliö                                          |
|4.Neliön pinta-ala                                     |
|5.Tasakylkisen kolmion pinta-ala                       |
|6.Suorakulmaisen kolmion hypotenuusa                   |
|                                                       |
|Q.Sammutaa ohjelman                                    |
|*******************************************************|\n
""")

def askchoice():
    validinput = False
    inp = -1 
    while(not validinput): 
        try:
            inp = input()
            if(inp=="Q" or inp=="q"):
                exit()
            val = int(inp)
            if(val<7 and val> 0):
                return val
            else:
                raise ValueError
        except ValueError:
            print("Virheellinen syöte. Anna numero 1-6")


if(__name__ == "__main__"):
    while(True):
        clearconsole()
        greeting()
        choice = askchoice()
        clearconsole()
        perus.startprog(choice)
