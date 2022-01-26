from entities import sensor


class Humidity(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Humidity"
