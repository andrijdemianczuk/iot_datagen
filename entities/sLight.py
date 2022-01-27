from entities import sensor


class Light(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Light"
        self.filePath = self.writeLocation + "Light_data.csv"
        self.newFilePath = self.writeLocation + "Light_data_" + self.guid + ".csv"
