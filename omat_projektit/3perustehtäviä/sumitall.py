import sys

if(__name__=="__main__"):
    if(len(sys.argv) > 1):
        sumall = 0
        for i in range(1,len(sys.argv)):
            try:
                sumall += int(sys.argv[i])
            except ValueError:
                print("Invalid values")
                exit()
        print(sumall)
