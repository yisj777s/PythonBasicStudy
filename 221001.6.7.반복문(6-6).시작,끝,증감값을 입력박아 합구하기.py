#시작,끝,증감값을 입력받아 합구하기
hap,num1,num2,num3=0,0,0,0

num1=int(input("시작 값을 입력하세요. : "))
num2=int(input("끝 값을 입력하세요. : "))
num3=int(input("증감 값을 입력하세요. : "))

for i in range(num1,num2+1,num3):
    hap+=i

print("%d부터 %d까지 %d씩 증가한 합은 %d입니다."%(num1,num2,num3,hap))