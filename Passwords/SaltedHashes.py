#################### Salted Hashes(Part 2)################

import hashlib

wl=open("wordList.txt","r")
wordL = wl.read().splitlines()

pw2 = open("password2.txt","r")
count=0
hashList = []
while True:
    count+=1
    line=pw2.readline()
    if not line:
        break
    x=line.split(",")
    hashList.append(x[0])
    hashList.append(x[4])

total=0
for i in range(len(wordL)):
    for j in range(len(wordL)):
        if(i!=j):
            words = wordL[i]+wordL[j]
            res = hashlib.md5(words.encode())
            if(res.hexdigest() == hashList[1]):
                print("Salt added to user "+ hashList[0]+" is "+wordL[i])
                total+=1
            elif(res.hexdigest() == hashList[3]):
                print("Salt added to user "+ hashList[2]+" is "+wordL[i])
                total+=1
            elif(res.hexdigest() == hashList[5]):
                print("Salt added to user "+ hashList[4]+" is "+wordL[i])
                total+=1
            if(total==3):
                break
            
