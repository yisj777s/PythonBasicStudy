aa=[]
bb=[]
value=0

for i in range(100):
    aa.append(value)
    value+=2
    
for j in range(100):
    bb.append(aa[99-j])
    
print("bb[0]=%d, bb[99]=%d"%(bb[0],bb[99]))