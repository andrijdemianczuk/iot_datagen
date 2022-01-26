from entities import sensor


class Light(sensor.Sensor):

    def __init__(self, writeLocation, srcLocation):
        super().__init__(writeLocation, srcLocation)
        self.name = "Light"
