class vehicles:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(vehicles):
    pass

school_bus = Bus("Schllo Volve, 180, 12)")
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.maxspeed, "Mileage:",
school_bus.mileage)