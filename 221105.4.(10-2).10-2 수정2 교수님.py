inFp=None
inStr=""
i=0
inFp=open("C:/temp/data1.txt","r",encoding='utf-8')

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    i+=1
    print("%d: %s"%(i,inStr),end="")
    
inFp.close()