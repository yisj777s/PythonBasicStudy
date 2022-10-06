List1=[]
List2=[]
value=1
for i in range(3):
    for k in range(4):
        List1.append(value)
        value+=1
    List2.append(List1)
    List1=[]
    
for i in range(3):
    for k in range(4):
        print("%3d"%List2[i][k],end=" ")
    print("")
    