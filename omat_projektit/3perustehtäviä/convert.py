import sys

if(__name__=="__main__"):
    if(len(sys.argv) == 2):
        try:
            num = float(sys.argv[1])
            print(f"{num} celciusta on {273.15+num} kelviniä.")
            print(f"{num} celciusta on {num*1.8+32} fahrenheitiä.")
        except ValueError:
            print("Virheellinen syöte")
            exit()


