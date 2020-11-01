from os import name,system,sys
import time 

#constants
MAX_BOARD_SIZE = 20
MIN_BOARD_SIZE = 3
#globals
streak = 0
nowinner = True
board = []


class Player:
    def __init__(self,name,marker):
        self.name 	= name
        self.marker = marker

def createboard(num):
    for i in range(num):
        board.append([])
        for j in range(num):
            board[i].append(" ")

def declarewinner(player):
    clearconsole()
    printboard()
    print(f"\nJippii, pelaaja {player.name} voitti pelin!")
    time.sleep(3)
    exit()

def checkdiag(players):
    for p in range(2):
        mark = players[p].marker
        markcount = 0
        for x in range(len(board)):
            for y in range(len(board)):
                if(x - streak >= 0 and y + streak <= len(board)): #upleft
                    for ul in range(streak):
                        if(board[x-ul][y+ul] == mark):
                            markcount+=1
                    if(markcount == streak):
                        declarewinner(players[p])
                        return
                markcount = 0
                if(x + streak <= len(board) and y + streak <= len(board)): #upright
                    for ul in range(streak):
                        if(board[x+ul][y+ul] == mark):
                            markcount+=1
                    if(markcount == streak):
                        declarewinner(players[p])
                        return
                markcount = 0
                if(x - streak >= 0 and y - streak >= 0): #downleft
                    for ul in range(streak):
                        if(board[x-ul][y-ul] == mark):
                            markcount+=1
                    if(markcount == streak):
                        declarewinner(players[p])
                        return
                markcount = 0
                if(x + streak <= len(board) and y - streak >= 0): #downright
                    for ul in range(streak):
                        if(board[x+ul][y-ul] == mark):
                            markcount+=1
                    if(markcount >= streak):
                        declarewinner(players[p])
                    markcount = 0


def checkhorizontal(players):
    markcount = 0
    for p in range(len(players)):
        player = players[p]
        for x in range(len(board)):
            for y in range(len(board)):
                if(y + streak <= len(board)):
                    for s in range(streak):
                        if(board[x][y+s] == player.marker):
                            markcount+=1
                    if(markcount >= streak):
                        declarewinner(player)
                    markcount = 0	

def checkvertical(players):
    markcount = 0
    for p in range(len(players)):
        player = players[p]
        for x in range(len(board)):
            for y in range(len(board)):
                if(x + streak <= len(board)):
                    for st in range(streak):
                        if(board[x+st][y] == player.marker):
                            markcount+=1
                    if(markcount>=streak):
                        declarewinner(player)
                    markcount = 0

def clearconsole():
    if(name == "nt"):
        system("cls")
    else:
        system("clear")

def printboard():
    row = 2
    char = 'A'
    for ind in range(len(board) + 1):
        if(ind==0):
            print(" ",end="")
        else:
            print(f"  {char}",end="")
            char = chr(ord(char)+1)
    print("")
    print("1 ",end="")
    for x in range(len(board)):
        for y in range(len(board[x])):
            print("[",end="")
            print(board[x][y],end="")
            print("]",end="")
        print("\n",end="")
        if(x<len(board)-1):
            if(row<10):
                print(str(row)+" ",end="")
            else:
                print(str(row)+"",end="")
        row+=1

def getwinner(players):
    boardlen = len(board)
    if(boardlen != len(board[0])):
        print("Väärän kokoinen pelilauta, voittajaa ei voida tarkastaa")
        exit()
    checkdiag(players)	
    checkhorizontal(players)
    checkvertical(players)

def validateinput(arg,player):
    if(len(arg) < 4):
        arg = arg.lower()
        boardlen = len(board[0])
        row = arg[1:len(arg)]
        x = 0
        try:
            x = int(row)
            if(x==0):
                return False
        except ValueError:
            return False
        if(ord(arg[0]) >= 97 and ord(arg[0]) <= 97 + boardlen):
            y = ord(arg[0]) - 97  
            x -= 1 
            if(board[x][y][0] == " "):
                board[x][y] = player.marker
                return True
    return False

def getboardsize():
    num = -1
    while(num<MIN_BOARD_SIZE or num>MAX_BOARD_SIZE):
        clearconsole()	
        print(f"Kuinka isolla ruudukolla haluat pelata? Syötä ruudukon sivun pituus. Esim 3 = 3x3 ruudukko.\nValitse arvo väliltä {MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}.")
        try:
            num = int(input())
        except ValueError:
            print(f"Syötä luku välillä {MIN_BOARD_SIZE} ja {MAX_BOARD_SIZE}")
            time.sleep(2)
            clearconsole()
            num = -1 #sanityyyyy
    return num

def setstreak():
    maxstreak = 0
    global streak	
    if(len(board) <= 4):
        streak = 3
        print("Automaattisesti valittu 3 peräkkäistä merkkiä voiton kriteeriksi.")
        return
    else:	
        maxstreak = len(board)-1
        while(streak<3 or streak>maxstreak):
            print(f"Aseta tarvittava määrä peräkkäisiä merkkejä voittoon väliltä {MIN_BOARD_SIZE} ja {maxstreak}.")
            try:
                streak = int(input())
            except ValueError:
                print("Virheellinen syöte")

def getuserinput(player):
    inp = False
    print(f"Pelaajan {player.name} vuoro.")
    while(not inp):
        qu = input("Syötä koordinaatit: ")
        inp = validateinput(qu,player)
        if(not inp):
            print("Virheellinen syöte")

if(__name__=="__main__"):
    clearconsole()
    player1_name = ""
    player2_name = ""
    if(len(sys.argv) > 1 and sys.argv[1]=="-d"): #debug stuff
        player1_name = "DEBUG1"
        player2_name = "DEBUG2"
        createboard(10)
        streak = 4
    else:
        boardsize = getboardsize()
        createboard(boardsize)
        setstreak()
        while(len(player1_name) <= 0):
            player1_name = input("Anna nimi pelaajalle 1\n")
        while(len(player2_name) <= 0):
            player2_name = input("Anna nimi pelaajalle 2\n")
        p1 = Player(player1_name,"X")
        p2 = Player(player2_name,"0")
        players = [p1,p2]
        gameround = 0
        clearconsole()
        while(nowinner):
            printboard()
            if(gameround == len(board) ** 2):
                print("\nTasapeli!")
                time.sleep(2)
                exit()
            if(gameround % 2 != 0):
                getuserinput(p1)
            else:
                getuserinput(p2)
            getwinner(players)
            gameround+=1
            clearconsole()
