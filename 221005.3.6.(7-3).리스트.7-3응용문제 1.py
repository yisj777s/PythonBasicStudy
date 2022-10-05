print("1~10번째 숫자 입력받아 합을 구하는 프로그램")
aa=[]
hap=0
for i in range(10):
    aa.append(0)
    
for i in range(10):
    aa[i]=int(input(str(i+1)+"번째 숫자 입력: "))

for i in range(10):
    hap+=aa[i]

print("입력받은 숫자들의 합: %d"%hap)