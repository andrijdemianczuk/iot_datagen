from entities import sensor


class Humidity(sensor.Sensor):

    def __init__(self, filetype="csv"):
        super().__init__()
        self.name = "Humidity"
        self.fileType = filetype
