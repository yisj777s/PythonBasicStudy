a=int(input("점수를 입력하세요: "))

if a>100 or a<0:
    print("잘못된 입력입니다.")
elif a>=90:
    print("A", end="")
elif a>=80:
    print("B", end="")
elif a>=70:
    print("C", end="")
elif a>=60:
    print("D", end="")
else:
    print("F", end="")

print("학점입니다.")