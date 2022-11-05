inFp=None
inStr=""
i=1
inFp=open("C:/temp/data1.txt","r",encoding='utf-8')

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print("%d: "%i,inStr,end="")
    i+=1
    
inFp.close()