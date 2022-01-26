from entities import sensor


class Pressure(sensor.Sensor):

    def __init__(self, writeLocation, srcLocation):
        super().__init__(writeLocation, srcLocation)
        self.name = "Pressure"
