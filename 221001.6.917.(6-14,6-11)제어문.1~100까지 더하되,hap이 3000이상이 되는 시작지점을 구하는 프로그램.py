from heapq import heappush


hap=0

for i in range(1,101):
    hap+=i
    if hap>=3000:
        break

print("1~100의 합에서 최초로 3000이 넘는 위치: %d,합: %d"%(i,hap))
