from car import Car
from truck import Truck
from garage import Garage


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