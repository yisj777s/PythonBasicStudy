#클래스 정의 부분
class Car:

    def __init__(self,value1,value2):
        self.color=value1
        self.speed=value2
    
    def upSpeed(self,value):
        self.speed+=value

    def downSpeed(self,value):
        self.speed-=value

#메인코드부분
myCar1=Car("보라",30)
myCar2=Car("검정",80)
myCar3=Car("주황",150)

print("자동차1의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar2.color,myCar2.speed))

print("자동차3의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar3.color,myCar3.speed))