from entities import sensor


class Prox(sensor.Sensor):

    def __init__(self, writeLocation, srcLocation):
        super().__init__(writeLocation, srcLocation)
        self.name = "Prox"
