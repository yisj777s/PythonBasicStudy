heartNum=0
numStr,ch="",""

numStr=input("숫자를 여려 개 입력하세요: ")
print("")

i=0
ch=numStr[i]
while True:
    heartNum=int(ch)

    heartStr=""
    for k in range(0,heartNum):
        heartStr+="\u2665"
        k+=i
    print(heartStr)
    
    i+=1
    if(i>len(numStr)-1):
        break
    
    ch=numStr[i]