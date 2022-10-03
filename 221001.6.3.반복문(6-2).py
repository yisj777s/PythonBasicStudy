#500에서 1000사이의 홀수의 합
hap = 0

for i in range(501,1000,2):
    hap+=i

print("500부터 1000사이의 홀수의 합은 %d입니다."%hap)