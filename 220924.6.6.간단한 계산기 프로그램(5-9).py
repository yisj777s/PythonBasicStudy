a,b,op =0,0,""

a=int(input("첫 번째 수를 입력하세요: "))
b=int(input("두 번째 수를 입력하세요: "))
op=input("계산할 연산자를 입력하세요: ")

if op=="+":
    print(" %d+%d=%d입니다. "%(a,b,a+b))
elif op=="-":
    print("%d-%d=%d입니다. "%(a,b,a-b))
elif op=="*":
    print("%d*%d=%d입니다. "%(a,b,a*b))
elif op=="/":
    print("%d/%d=%d입니다. "%(a,b,a/b))
elif op=="//":
    print("%d//%d=%d입니다. "%(a,b,a//b))
elif op=="%":
    print("%d%%%d=%d입니다. "%(a,b,a%b))
elif op=="**":
    print("%d**%d=%d입니다. "%(a,b,a**b))
else:
    print("잘못 입력된 연산자입니다.")