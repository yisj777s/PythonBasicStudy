ch=""
a,b=0,0

while True:
    a=int(input("계산할 첫 번째 수 입력: "))
    b=int(input("계산할 첫 번째 수 입력: "))
    ch=input("계산할 연사자를 입력: ")
    
    if(ch=="+"):
        print("%d+%d=%d입니다."%(a,b,a+b))
    elif(ch=="-"):
        print("%d-%d=%d입니다."%(a,b,a-b))
    elif(ch=="*"):
        print("%d*%d=%d입니다."%(a,b,a*b))
    elif(ch=="/"):
        print("%d/%d=%d입니다."%(a,b,a/b))
    elif(ch=="%"):
        print("%d%%%d=%d입니다."%(a,b,a%b))
    elif(ch=="//"):
        print("%d//%d=%d입니다."%(a,b,a//b))
    elif(ch=="**"):
        print("%d**%d=%d입니다."%(a,b,a**b))
    else:
        print("연산자를 잘못 입력했습니다.")
        
    