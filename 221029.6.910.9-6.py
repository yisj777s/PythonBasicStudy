def func1():
    a = 10 #지역변수
    print("func1()에서 a의 값 %d"%a)

def func2():
    print("fun2()에서 b의 값 %d"%b)

b=20 #전역변수

func1()
func2()
print("%d %d"%(a,b))