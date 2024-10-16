
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




class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)
        self.winter_tires = winter_tires

    def toString(self):
        base_string = super().toString()
        return f"{base_string}\nHas winter tires: {self.winter_tires}"

class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def toString(self):
        base_string = super().toString()
        return f"{base_string}\nHas trailer: {self.trailer}"





