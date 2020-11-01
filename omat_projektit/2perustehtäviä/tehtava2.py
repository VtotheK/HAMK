import sys

if(len(sys.argv) < 2):
    print("Ei komentoriviargumentteja")
    exit()

arg = sys.argv[1]
for i in range(len(arg)//2):
    if(arg[i] != arg[len(arg)-(i+1)]):
        print("Sana ei ole palindromi")
        exit()
print("Sana on palindromi")
