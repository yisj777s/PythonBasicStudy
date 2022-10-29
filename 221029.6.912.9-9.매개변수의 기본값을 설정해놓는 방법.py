def para_func(v1,v2,v3=0):
    result=0
    result=v1+v2+v3
    return result

hap=0

hap=para_func(10,20)
print("매개변수 2개 함수 호출 결과==>%d"%hap)

hap=para_func(10,20,30)
print("매개변수 3개 함수 호출 결과==>%d"%hap)