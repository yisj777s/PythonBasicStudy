student1={'학번':1000,'이름':'홍길동','학과':'열공학과'}
print(student1)
#연락처 추가
student1['연락처']='010-1111-2222'
print(student1)
#이미 있는 키를 사용하면 기존의 값이 수정(변경)
student1['학과']='파이썬학과'
print(student1)
#del(딕셔너리이름[키])함수를 사용하여 삭제
del(student1['연락처'])
print(student1)
