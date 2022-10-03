#1에서 100까지의 짝수의 합과 홀수의 합을 구하세요.
hap1,hap2=0,0

for i in range(1,101,1):
    if i%2==0:
        hap1+=i
    else:
        hap2+=i

print("1~100까지의 짝수의 합은 %d입니다."%hap1)
print("1~100까지의 홀수의 합은 %d입니다."%hap2)