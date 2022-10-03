#각 단의 출력이 몇 단인지 표시하세요.
for i in range(2,10):
    print("%d단:"%i)
    for j in range(1,10):
        print("%dX%d=%2d"%(i,j,i*j))