class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass = 25
        thickness = 5
        return mass * thickness * self._length * self._width / 1000


some_road = Road(20, 5000)
print(f"{some_road.asphalt_mass()}T")
