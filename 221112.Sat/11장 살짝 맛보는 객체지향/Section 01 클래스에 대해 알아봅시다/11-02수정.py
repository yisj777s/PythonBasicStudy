class Car:
    color=""
    speed=0

    def upSpeed(self,value):
        self.speed+=value
        if self.speed>150:
           self.speed=150

    def downSpeed(self,value):
        self.speed-=value
        if self.speed<0:
            self.speed=0

#메인코드부분
myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0

myCar1.upSpeed(170)
myCar1.downSpeed(200)
print("자동차1의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar1.color,myCar1.speed))

myCar2.upSpeed(30)
myCar2.downSpeed(60)
myCar2.upSpeed(90)
print("자동차2의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar2.color,myCar2.speed))

myCar3.upSpeed(90)
myCar3.downSpeed(120)
myCar3.upSpeed(290)
print("자동차3의 색상은 %s이며,  현재속도는 %dkm 입니다."%(myCar3.color,myCar3.speed))

    