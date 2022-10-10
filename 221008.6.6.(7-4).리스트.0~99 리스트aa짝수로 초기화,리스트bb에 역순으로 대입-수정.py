aa=[]
bb=[]

for i in range(0,200,2):
    aa.append(i)

print(aa[1:6])
    
for j in range(100):
    bb.append(aa[99-j])

print(bb)
print("bb[0]=%d, bb[99]=%d"%(bb[0],bb[99]))