import sys

if(len(sys.argv) < 2):
    print("Ei komentoargumenttia.")
    exit() 

dic = {}
arg = str(sys.argv[1])
count = 0
for i in range(len(arg)):
    if(dic.get(arg[i])):
        dic[arg[i]] += 1 
    else:
        dic[arg[i]] = 1
        count += 1
print(f"Löydettiin {count} erilaista merkkiä")

for key,val in dic.items():
    print(f"merkki:{key} määrä:{val}")
