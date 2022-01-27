from entities import sensor


class Humidity(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Humidity"
        self.filePath = self.writeLocation + "Humidity_data.csv"
        self.newFilePath = self.writeLocation + "Humidity_data_" + self.guid + ".csv"