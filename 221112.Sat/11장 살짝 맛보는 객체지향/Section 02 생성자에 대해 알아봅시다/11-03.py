#클래스 정의 부분
class Car:

    def __init__(self):
        self.color="빨강"
        self.speed=0
    
    def upSpeed(self,value):
        self.speed+=value

    def downSpeed(self,value):
        self.speed-=value

#메인코드부분
myCar1=Car()
myCar2=Car()

print("자동차1의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar2.color,myCar2.speed))