from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  
        self.has_trailer = has_trailer

    def toString(self):
        base_class_func = super().toString()
        return f"{base_class_func}\nHas trailer: {self.has_trailer}"