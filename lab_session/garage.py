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