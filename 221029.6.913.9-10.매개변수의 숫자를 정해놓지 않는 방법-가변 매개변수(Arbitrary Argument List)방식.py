def para_func(*para):
    result=0
    for num in para:
        result+=num
    return result

    
hap=0

hap=para_func(10,20)
print("매개변수 2개 함수 호출 결과==> %d"%hap)
hap=para_func(10,20,30,40,50,60,70)
print(hap)