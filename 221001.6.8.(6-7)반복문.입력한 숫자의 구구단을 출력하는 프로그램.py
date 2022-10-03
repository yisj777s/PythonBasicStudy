#단을 입력받아 구구단 출력 프로그램
dan=0

dan=int(input("몇 단?:"))

for i  in range(1,10):
    print("%dX%d=%2d"%(dan,i,dan*i))