import csv
import time
import random
import uuid
import os
from datetime import datetime

import entities.sHumidity
from entities import *

if __name__ == '__main__':

    # Params
    guid = str(uuid.uuid4())
    fileStore = "temp/"
    filePath = fileStore + "Humidity_data.csv"
    newFilePath = fileStore + "Humidity_data_" + guid + ".csv"
    fileIsEmpty = False

    # Hourly seasonality
    offsetHr = {"0": 0.68, "1": 0.69, "2": 0.7, "3": 0.66, "4": 0.65, "5": 0.72, "6": 0.85, "7": 0.88, "8": 0.9,
                "9": 0.94,
                "10": 1.0, "11": 1.1, "12": 1.17, "13": 1.15, "14": 1.11, "15": 1.1, "16": 0.99, "17": 0.97, "18": 0.95,
                "19": 0.9, "20": 0.7, "21": 0.72, "22": 0.75, "23": 0.7}

    # Daily seaonality
    offsetDay = {"0": 1.0, "1": 1.0, "2": 1.0, "3": 1.0, "4": 1.0, "5": 0.9, "6": 0.9}  # Monday is 0 Sunday is 6

    # fileRolloverLimitB = 10485760 #10Mb per file
    fileRolloverLimitB = 1048576  # 1MB per file

    # Open the file if exists and append, otherwise create a new one at the specified file path
    f1 = open(filePath, "a")

    # Set a flag to check if the file is empty.
    if os.stat(filePath).st_size == 0:
        fileIsEmpty = True

    # Open the source (template) file, only write the header if the file is new
    with open('IoT_Sensor_Template/Humidity.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        dayOfWeek = datetime.today().weekday()  # used to modify for weekends / non-business days
        d = datetime.fromtimestamp(epoch_time)  # used for random offset by hour-of-day
        offset = offsetHr[str(d.hour)] * offsetDay[str(dayOfWeek)]

        # If the file is already established, skip writing the header
        if not fileIsEmpty:
            next(reader)

        # Write each row with replacements
        for row in reader:
            if row[2] == "0":
                row[2] = epoch_time
            if row[1] == "0":  # Change the value range based on location
                if 1 <= int(row[3]) <= 130:  # Seattle
                    row[1] = random.randint(55, 85) * offset
                elif 131 <= int(row[3]) <= 420:  # Portland
                    row[1] = random.randint(50, 75) * offset
                elif 421 <= int(row[3]) <= 835:  # San Francisco
                    row[1] = random.randint(65, 80) * offset
                elif 836 <= int(row[3]) <= 880:  # Helena
                    row[1] = random.randint(35, 55) * offset
                else:  # Boise
                    row[1] = random.randint(20, 50) * offset
            rowStr = str(row)
            f1.write(
                str(row).translate({ord(i): None for i in '[]\''}))  # Remove the unwanted characters '[', ']' and '''
            f1.write("\r\n")
    f1.close()

    # Rollover the file if it's greater or equal to the limit.
    if os.stat(filePath).st_size >= fileRolloverLimitB:
        os.rename(filePath, newFilePath)
