from entities import sensor


class Temp(sensor.Sensor):

    def __init__(self, filetype="csv"):
        super().__init__()
        self.name = "Temp"
        self.fileType = filetype
