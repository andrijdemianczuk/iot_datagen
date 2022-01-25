import csv
import time
import random
import uuid
import os

if __name__ == '__main__':

    #Params
    guid = str(uuid.uuid4())
    fileStore = "temp/"
    filePath = fileStore + "Humidity_data.csv"
    newFilePath = fileStore + "Humidity_data_" + guid + ".csv"
    fileIsEmpty = False

    #fileRolloverLimitB = 10485760 #10Mb per file
    fileRolloverLimitB = 1048576 #1MB per file

    #Open the file if exists and append, otherwise create a new one at the specified file path
    f1 = open(filePath, "a")

    #Set a flag to check if the file is empty.
    if os.stat(filePath).st_size == 0: fileIsEmpty = True

    #Open the source (template) file, only write the header if the file is new
    with open('IoT_Sensor_Template/Humidity.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())

        #If the file is already established, skip writing the header
        if not fileIsEmpty : next(reader)

        #Write each row with replacements
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            rowStr = str(row)
            f1.write(str(row).translate({ord(i): None for i in '[]\''}))  # Remove the unwanted characters '[', ']' and '''
            f1.write("\r\n")
    f1.close()

    #Rollover the file if it's greater or equal to the limit.
    if os.stat(filePath).st_size >= fileRolloverLimitB: os.rename(filePath, newFilePath)