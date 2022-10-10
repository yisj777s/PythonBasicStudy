aa=[]
for i in range(10):
    aa.append(0)
    
for i in range(10):
    aa[i]=int(input(str(i+1)+"번째 숫자: "))
hap=0
for i in range(10):
    hap+=aa[i]
print("합계: %d"%hap)

