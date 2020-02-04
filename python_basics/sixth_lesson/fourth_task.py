from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car's moving!")

    def stop(self):
        print("The car have stopped!")

    def turn(self):
        self.side = ("left", "right")
        print(f"The car have turned to the {self.side[randint(0,1)]}")

    def show_speed(self):
        print(f"Speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Speed is {self.speed}")
        if self.speed > 60:
            print("You are exceeding the speed limit!!!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Speed is {self.speed}")
        if self.speed > 40:
            print("You are exceeding the speed limit!!!")


class SportCar(Car):
    counter = 0

    def change_tires(self):
        SportCar.counter += 1
        if SportCar.counter % 2 == 0:
            print("Tires changed for rain")
        else:
            print("Tires changed to slick")


class PoliceCar(Car):
    def start_pursuit(self):
        print("We have started pursuit!!!")


toyota = Car(50, "red", "toyota", False)

gazel = WorkCar(50, "green", "gazel", False)

bmw = SportCar(100, "yellow", "bmw", False)

musorovoz = PoliceCar(50, "durty", "lada", True)

toyota.go()
toyota.turn()
toyota.turn()
toyota.turn()
toyota.stop()
gazel.show_speed()
bmw.change_tires()
bmw.change_tires()
bmw.change_tires()
musorovoz.start_pursuit()
print(musorovoz.speed)
