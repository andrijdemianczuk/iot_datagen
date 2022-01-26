from entities import sensor


class Pressure(sensor.Sensor):

    def __init__(self, filetype="csv"):
        super().__init__()
        self.name = "Pressure"
        self.fileType = filetype
