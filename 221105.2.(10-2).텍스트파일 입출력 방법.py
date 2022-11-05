inFp=None
inStr=""

inFp=open("C:/temp/data1.txt","r",encoding='utf-8')

while True:
    inStr=inFp.readline()
    if inStr=="":
        break;
    print(inStr,end="")

inFp.close()