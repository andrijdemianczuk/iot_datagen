from entities import sensor


class Temp(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Temp"
        self.filePath = self.writeLocation + "Temp_data.csv"
        self.newFilePath = self.writeLocation + "Temp_data_" + self.guid + ".csv"