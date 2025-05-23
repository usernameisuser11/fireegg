class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        print("현재 속도(슈퍼클래스): %d" % self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브클래스 - Sedan): %d" % self.speed)

class Sonata(Sedan):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브클래스 - Sonata): %d" % self.speed)

class Truck(Car):
    pass

# 객체 생성
truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

# 속도 테스트
print("트럭 -->", end="")
truck1.upSpeed(200)  # Car 클래스의 기본 메서드

print("승용차 -->", end="")
sedan1.upSpeed(200)  # 최대 150

print("소나타 -->", end="")
sonata1.upSpeed(200)  # 최대 180
