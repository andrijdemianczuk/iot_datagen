import csv
import time
import random
import uuid
import os

if __name__ == '__main__':

    guid = str(uuid.uuid4())
    fileStore = "temp/"
    filePath = fileStore + "Humidity_data.csv"
    newFilePath = fileStore + "Humidity_data_" + guid + ".csv"
    fileIsEmpty = False

    #fileRolloverLimitB = 10485760 #10Mb per file
    fileRolloverLimitB = 1048576 #1MB per file

    f1 = open(filePath, "a")

    if os.stat(filePath).st_size == 0: fileIsEmpty = True

    if fileIsEmpty:
        print("creating new file")
    else:
        print("appending existing file")

    with open('IoT_Sensor_Template/Humidity.csv') as f:
        reader = csv.reader(f)
        next(reader)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            rowStr = str(row)
            f1.write(
                str(row).translate({ord(i): None for i in '[]\''}))  # Remove the unwanted characters '[', ']' and '''
            f1.write("\r\n")
    f1.close()

    if os.stat(filePath).st_size <= fileRolloverLimitB:
        print("File is less than limit. Current file size (MB) is: " + str(os.stat(filePath).st_size/1024/1024))
    else:
        print("doing rollover")
        os.rename(filePath, newFilePath)