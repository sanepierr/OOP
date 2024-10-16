from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)  
        self.winter_tires = winter_tires

    def toString(self):
        base_class_func = super().toString()
        return f"{base_class_func}\nHas winter tires: {self.winter_tires}"