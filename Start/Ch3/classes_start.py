# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, engineType):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.engine = engineType
  
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "Car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, engineType, hasSideCar):
    super().__init__("Motorcycle")
    if hasSideCar == True:
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.engine = engineType

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "Motorcycle at", self.speed)

class SportsCar(Car):
  def __init__(self, engineType, hp):
    super().__init__(engineType)
    self.hp = hp
    self.doors = 2

  def drive(self, speed):
    super().drive(speed)
    print("Driving my SportsCar", self.engine, "Car at", self.speed, ". It has", self.hp, "horsepower")


car1 = Car("unleaded")
car2 = Car("electric")
spCar1 = SportsCar("unleaded", 220)
mc1 = Motorcycle("unleaded", True)

print(mc1.wheels)
print(spCar1.wheels)

spCar1.drive(30)

