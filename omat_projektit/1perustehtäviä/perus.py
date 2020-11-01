from math import sqrt
import main 
class NegativeNumberError(Exception):
    def __init__(self,message):
        self.message = message

multi   = lambda x,y: x*y
square  = lambda x: x**2

def askretry():
    while(True):
        print("Haluatko käynnistää ohjelman uudestaan? k/e")
        ip = input()
        if(ip == "k"):
            return
        elif(ip == "e"):
            exit()
        else:
            app.clearconsole()
            print("Väärä syöte")

def getnums(message,amount,onlypositive):
    print(message)
    delim = merkki = num = ""
    if(amount==1):
        delim   = "luku"
        merkki  = "merkki"
        num     = "numero"
    else:
        delim   = "lukua"
        merkki  = "merkit"
        num     = "numeroita"
    while(True):
        userinput = input().split() 
        if(len(userinput) != amount):
            print(f"Syötä {amount} {delim}.")
        else:
            try:
                out = []
                for i in range(len(userinput)):
                    if(onlypositive and float(userinput[i]) <= 0):
                        if(amount > 1):
                            raise NegativeNumberError("Syötä vain lukuja mitkä >0")
                        else:
                            raise NegativeNumberError("Syötä vain luku mikä >0")
                    out.append(float(userinput[i]))
                return out
            except ValueError:
                print(f"Syöttämäsi {merkki} ei ole {num}.")
            except NegativeNumberError as negerror:
                print(negerror.message)


def yhteenlasku():
    val = 0
    numone = numtwo = "" 
    nums = getnums("Syötä kaksi numeroa yhteenlaskettavaksi välilyönnillä eroteltuna",2,False)
    for num in nums:
        val += num
    if (nums[1] < 0):
        numtwo = "(" + str(nums[1]) + ")"
    else:
        numtwo = str(nums[1])
    numone = str(nums[0])
    print(f"{numone} + {numtwo} = {val}")
    


def startprog(choice): 
    if(choice==1):
        print("Hello world!")
    elif(choice==2):
        yhteenlasku()
    elif(choice==3):
        msg = "Syötä luku minkä neliö halutaan laskea"
        sq = getnums(msg,1,False)
        print(f"Luvun {sq[0]} neliö on {square(sq[0])}.")
    elif(choice==4):
        msg = "Syötä neliön sivun pituus"
        sqarea = getnums(msg,1,True)
        print(f"Neliön sivun pituuden ollessa {sqarea[0]}, neliön pinta-ala on {multi(sqarea[0],sqarea[0])}")
    elif(choice==5):
        msg = "Syötä tasakylkisen kolmion kannan leveys, sekä kolmion korkeus välilyönnillä eroteltuna"
        nums = getnums(msg,2,True)
        print(f"Kolmion pinta-ala on {multi(nums[0],nums[1])/2}.")
    elif(choice==6):
        msg = "Syötä suorakulmaisen kolmion kateettien pituudet välilyönnillä eroteltuna."
        nums = getnums(msg,2,True)
        hypo = sqrt(square(nums[0]) + square(nums[1]))
        print(f"Kolmion jonka kateettien pituudet ovat {nums[0]} ja {nums[1]}, hypotenuusan pituus on {hypo}")
    askretry() 
