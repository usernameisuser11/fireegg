class Car :
    name =""
    speedd = 0

    def __int__(self, name, speed):
        self.name = name
        self.speed = speed


    def getName(self) :
        return self.name
    
    def getSpped(self) :
        return self.speed
    
    car1, car2 = None, None

    car1 = car1("아우디", 0)
    car2 = car2("벤츠", 30)

    print("%s의 현재 속도는 %d 입니다." % (car1.getName(), car1.getSpped()))
    print("%s의 현재 속도는 %d km 입니다." % (car2.getName(), car2.getSpped()))