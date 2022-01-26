from entities import sensor


class Light(sensor.Sensor):

    def __init__(self, filetype="csv"):
        super().__init__()
        self.name = "Light"
        self.fileType = filetype
