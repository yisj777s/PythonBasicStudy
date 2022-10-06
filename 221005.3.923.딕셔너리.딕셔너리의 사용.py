student1={'학번':1234,'이름':'홍길당','학과2':'파이썬학과'}
print(student1['학번'])     
print(student1['학과2']) 
print(student1['이름'])     
#딕셔너리이름.get(키) 함수
print(student1.get('학번'))

#딕셔너리이름.keys()함수 - 딕셔너리의 모든 키 반환
print(student1.keys())
#list(딕셔너리이름.keys()) 함수- 앞에 dict_keys를 뺴고 리스트
print(list(student1.keys()))
#.values() 함수-딕셔너리의 모든 값 반환
print(student1.values())
#마찬가지 list로 하면 앞 삭제후 리스트 형태로
print(list(student1.values()))
#.ltems()함수-튜플 형태
print(student1.items())
#in - 딕셔너리에 키가 있으면 True를, 없으면 False반환
print('이름' in student1)
print('이름2' in student1)
print('주소' in student1)
    