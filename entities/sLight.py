import csv
import random
from entities import sensor


class Light(sensor.Sensor):

    def __init__(self, writeLocation: str, srcLocation: str) -> None:
        super().__init__(writeLocation, srcLocation)
        self.srcName = "Light.csv"
        self.filePath = self.writeLocation + "Light_data.csv"
        self.newFilePath = self.writeLocation + "Light_data_" + self.guid + ".csv"

    def processObjFile(self, srcFile, f1):
        # Open the source (template) file, only write the header if the file is new
        with open(srcFile) as f:
            reader = csv.reader(f)
            # If the file is already established, skip writing the header
            if not self.fileIsEmpty:
                next(reader)

            # Write each row with replacements
            for row in reader:
                if row[2] == "0":
                    row[2] = self.epoch_time
                if row[1] == "0":  # Change the value range based on location
                    if 1 <= int(row[3]) <= 130:  # Seattle
                        row[1] = round(random.randint(55, 85) * self.offset, 2)
                    elif 131 <= int(row[3]) <= 420:  # Portland
                        row[1] = round(random.randint(50, 75) * self.offset, 2)
                    elif 421 <= int(row[3]) <= 835:  # San Francisco
                        row[1] = round(random.randint(65, 80) * self.offset, 2)
                    elif 836 <= int(row[3]) <= 880:  # Helena
                        row[1] = round(random.randint(35, 55) * self.offset, 2)
                    else:  # Boise
                        row[1] = round(random.randint(20, 50) * self.offset, 2)
                # rowStr = str(row)
                f1.write(
                    str(row).translate(
                        {ord(i): None for i in '[]\''}))  # Remove the unwanted characters '[', ']' and '''
                f1.write("\r\n")
        f1.close()