class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# TrackedVehicle is a subclass of vehicle can be checked.
print(issubclass(TrackedVehicle, Vehicle))

# LandVehicle is a subclass of TrackedVehicle can be checked.
print(issubclass(LandVehicle, TrackedVehicle))

vehicle = Vehicle()
land = LandVehicle()
tracked = TrackedVehicle()

# tracked object is an instance of Vehicle or not is checked.
print(isinstance(tracked, Vehicle))

# vehicle object is an instance of LandVehicle or not is checked.
print(isinstance(vehicle, LandVehicle))

