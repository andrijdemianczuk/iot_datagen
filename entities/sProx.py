from entities import sensor


class Prox(sensor.Sensor):

    def __init__(self, filetype="csv"):
        super().__init__()
        self.name = "Prox"
        self.fileType = filetype
