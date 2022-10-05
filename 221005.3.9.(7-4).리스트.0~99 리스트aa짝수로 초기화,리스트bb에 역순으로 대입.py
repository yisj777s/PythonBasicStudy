aa=[]
bb=[]
value=0

for i in range(100):
    aa.append(value)
    value+=2

for i in range(100):
    bb.append(aa[99-i])

print("bb[0]은 %d,bb[99]는 %d"%(bb[0],bb[99]))