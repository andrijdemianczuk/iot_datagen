import csv
import time
import random
import uuid

if __name__ == '__main__':

    guid = uuid.uuid4()

    f1 = open("temp/Humidity.csv", "a")
    #f1.write("Now the file has more content!")
    #f1.close()
















    with open('IoT_Sensor_Template/Humidity.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0,100)
            rowStr = str(row)
            f1.write(str(row).translate({ord(i): None for i in '[]\''})) #Remove the unwanted characters '[', ']' and '''
            f1.write("\r\n")
    f1.close()



































    # with open('IoT_Sensor_Template/Light.csv') as f:
    #     reader = csv.reader(f)
    #     epoch_time = int(time.time())
    #     for row in reader:
    #         if (row[2] == "0"):
    #             row[2] = epoch_time
    #         if (row[1] == "0"):
    #             row[1] = random.randint(0, 100)
    #         print(row)
    #
    # with open('IoT_Sensor_Template/Pressure.csv') as f:
    #     reader = csv.reader(f)
    #     epoch_time = int(time.time())
    #     for row in reader:
    #         if (row[2] == "0"):
    #             row[2] = epoch_time
    #         if (row[1] == "0"):
    #             row[1] = random.randint(0, 100)
    #         print(row)
    #
    # with open('IoT_Sensor_Template/Prox.csv') as f:
    #     reader = csv.reader(f)
    #     epoch_time = int(time.time())
    #     for row in reader:
    #         if (row[2] == "0"):
    #             row[2] = epoch_time
    #         if (row[1] == "0"):
    #             row[1] = random.randint(0, 100)
    #         print(row)
    #
    # with open('IoT_Sensor_Template/Temp.csv') as f:
    #     reader = csv.reader(f)
    #     epoch_time = int(time.time())
    #     for row in reader:
    #         if (row[2] == "0"):
    #             row[2] = epoch_time
    #         if (row[1] == "0"):
    #             row[1] = random.randint(0, 100)
    #         print(row)