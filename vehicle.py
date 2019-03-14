class Vehicle(object):
    """docstring for Vehicle"""
    def __init__(self, model="", reg=0, speed=0, capacity=0, consume=0):
        self.model = model
        self.reg = reg
        self.speed = speed
        self.capacity = capacity
        self.consume = consume

    def setter():
        self.model = input("Enter Vehicle Model: ")
        self.reg = int(input("Enter Vehicle Registration no. : "))
        self.speed = float(input("Enter Speed (km/h): "))
        self.capacity = int(input("Enter fuel capacity (litres): "))
        self.consume = float(input("Enter fuel consumption (km/litres): "))


    def fuelneeded(self,distance):
        return (distance/self.consume)

    def distancecovered(self,time):
        return (self.speed * time)

    def display(self):
        print(f"Vehicle Model: {self.model} ")
        print(f"\nRegistration no. : {self.reg} ")
        print(f"\nVehicle Speed: {self.speed} km/h")
        print(f"\nFuel Capacity: {self.capacity} litres")
        print(f"\nFuel consumption: {self.consume} km/litre")


class Truck(Vehicle):
    """docstring for Truck"""
    def __init__(self, cargo=0):
        super(Vehicle, self).__init__()
        self.cargo = cargo
        
    def setter:
        self.cargo = int(input("Enter Cargo weight Limit: (kgs)"))