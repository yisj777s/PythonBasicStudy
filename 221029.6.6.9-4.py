def plus(v1,v2):
    result=0 #지역변수
    result=v1+v2
    return result

hap=0 #전역변수

hap=plus(300,400)
print("100과 200의 plus()함수 결과는 %d"%hap)