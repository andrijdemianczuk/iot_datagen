from entities import sensor


class Pressure(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Pressure"
        self.filePath = self.writeLocation + "Pressure_data.csv"
        self.newFilePath = self.writeLocation + "Pressure_data_" + self.guid + ".csv"
