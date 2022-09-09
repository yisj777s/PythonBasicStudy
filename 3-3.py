myVar=100
print(type(myVar))
myVar=100.0
print(type(myVar))
boolVar=False
intVar=100
floatVar=123.45
strVar="안녕?"
print(boolVar)
var2=300
var1=var2+20
print(var1)#된다
print("%d %d" %(var1,var2))
var3=400
var3=var3+500
print("%d" % var3)
var4=var5=var6=var7=100
print(var4)
a=123
print(type(a))
a=100**1000
print(a)
a,b=9,2
print(a**b, a%b,a//b)

a=True
print(type(a))

a = (100==100)
b = (10>100)
print(a, b)

#문자열 데이터 형식

a = "파이썬 만세"
print(a)
print(type(a))

print("작은따옴표는 ' 모양입니다.")
print('큰따옴표는 " 모양입니다.')
print("큰따옴표는 \" 모양입니다.")

a = "이건 큰따옴표 \" 모양."
b = '이건 작은땅모표 \'모양.'
print(a,b)

a = '파이썬 \n만세'
print(a)

a = """파이썬
만세"""
print(a)

print('파이썬\n만세')
