import sys

def minmax(num1,num2):
    return num1 if num1>num2 else num2

if(__name__=="__main__"):
    if(len(sys.argv) == 3):
        try:
             a = float(sys.argv[1])
             b = float(sys.argv[2])
             c = minmax(a,b)
             print(c)
        except ValueError:
            print("Virheellinen syöte")
    else:
        print("Virheellinen syöte")
