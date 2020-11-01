import random


def rollDie():
    return random.randint(1,6)  # Palauttaa kokonaisluvun väliltä 1-6

def main():
    try:
        print("Montako kertaa noppaa heitetään?")
        inp = int(input())
    except ValueError:
        print("Virheellinen syöte")

    r = 1
    p1wins = p2wins = 0
    for i in range(inp):
        p1res = rollDie()
        p2res = rollDie()
        if(p1res > p2res):
            p1wins+=1
            print(f"Kierroksen {i+1}. Pelaaja 1 voitti pelin")
        elif(p1res < p2res):
            p2wins+=1
            print(f"Kierroksen {i+1}. Pelaaja 2 voitti pelin")
        else:
            print("Tasapeli")
        r+=1
    if(p1wins>p2wins):
        winner = "Pelaaja 1"
    elif(p1wins<p2wins):
        winner = "Pelaaja 2"
    else:
        print(f"Peli päättyi tasapeliin, {p1wins}-{p2wins}")
        exit()
    print(f"Pelattuja kierroksia {r}, pisteet {p1wins}-{p2wins}, {winner} voitti pelin ")
main()
