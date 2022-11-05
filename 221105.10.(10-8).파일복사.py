inFp,outFp=None,None
inStr=""

inFp=open("c:/temp/data1.txt","r",encoding='utf-8')
outFp=open("c:/temp/data4.txt","w",encoding='utf-8')

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---정상적으로 파일이 복사되었음---")