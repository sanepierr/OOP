
class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"This vehicle is {self.color}"



class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)  
        self.winter_tires = winter_tires

    def toString(self):
        base_class_func = super().toString()
        return f"{base_class_func}\nHas winter tires: {self.winter_tires}"



class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  
        self.has_trailer = has_trailer

    def toString(self):
        base_class_func = super().toString()
        return f"{base_class_func}\nHas trailer: {self.has_trailer}"



class Garage:
    def __init__(self):
        self.parked_vehicle = []

    def setVehicle(self, vehicle):
        self.parked_vehicle.append(vehicle)  

    def toString(self):
        if self.parked_vehicle:
            descriptions = "\n".join(vehicle.toString() for vehicle in self.parked_vehicle)
            return f"Description of the parked vehicle(s):\n{descriptions}"
        else:
            return "The garage is empty"



#GARAGE_TESTER
class GarageTester:
    def __init__(self):
        self.garage = Garage()

    def addVehicles(self):
        # Create instances of Car and Truck
        car1 = Car("red", winter_tires=True)
        truck1 = Truck("blue", has_trailer=True)

        # Park vehicles in the garage
        self.garage.setVehicle(car1)
        self.garage.setVehicle(truck1)

    def runTest(self):
        self.addVehicles()
        print(self.garage.toString())


tester = GarageTester()
tester.runTest()






