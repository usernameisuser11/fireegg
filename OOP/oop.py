class Car:
    color = ""
    speed = 0

    def upsSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150  

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0  

myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "yellow"
myCar3.speed = 0

# 속도 증가
myCar1.upsSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %d km 입니다." % (myCar1.color, myCar1.speed))

myCar2.upsSpeed(160)  
print("자동차2의 색상은 %s 이며, 현재 속도는 %d km 입니다." % (myCar2.color, myCar2.speed))

myCar3.upsSpeed(0)
print("자동차3의 색상은 %s 이며, 현재 속도는 %d km 입니다." % (myCar3.color, myCar3.speed))
