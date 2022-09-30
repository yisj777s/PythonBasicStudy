numStr,ch="",""

numStr=input("숫자를 여러개 입력하세요.: ")
print("")

for i in range(len(numStr)):
    ch=numStr[i]
    heartNum=int(ch)
    heartStr=""
    
    for j in range(heartNum):
        heartStr+="\u2665"
    
    print(heartStr)