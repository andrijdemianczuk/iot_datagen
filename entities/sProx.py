from entities import sensor


class Prox(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.name = "Prox"
        self.filePath = self.writeLocation + "Prox_data.csv"
        self.newFilePath = self.writeLocation + "Prox_data_" + self.guid + ".csv"
