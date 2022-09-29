import random

count=0
numbers=[]
for num in range(10):
    numbers.append(random.randrange(1,7))
print("생성된 리스트", numbers)

for num in range(10):
    if numbers[num]==1:
        count += 1

print("%d이 %d번 나왔네요."%(1, count))