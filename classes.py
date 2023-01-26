

class Vehicle:

    def __init__(self, brand, number_of_wheels, color):
        self.brand = brand
        self.number_of_wheels = number_of_wheels
        self.color = color
        self.speed = 0

    def speed_up(self):
        self.speed += 1

    def move(self):
        print("it's moving at " + str(self.speed))

class Scooter(Vehicle):
    pass

def potato():
    pass

class Motorcycle(Vehicle):

    def __init__(self, brand, color, cubic_centimeters = 250):
        super().__init__(brand=brand, number_of_wheels=2, color=color)
        self.cubic_centimeters = cubic_centimeters


ford_car = Vehicle(brand="Ford", number_of_wheels=4, color="brown")
yamaha_motorcycle = Motorcycle("yamaha", "red")
        
print(ford_car.brand)

ford_car.move()

print(yamaha_motorcycle.brand)

yamaha_motorcycle.move()

ford_car.speed_up()
yamaha_motorcycle.speed_up()
ford_car.move()
yamaha_motorcycle.move()




#print(type(yamaha_motorcycle.cubic_centimeters))