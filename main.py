import csv
import time
import random
import asyncio

if __name__ == '__main__':
    with open('IoT_Sensor_Template/Humidity.csv') as f:
       reader = csv.reader(f)
       epoch_time = int(time.time())
       for row in reader:
           if (row[2] == "0"):
               row[2] = epoch_time
           if (row[1] == "0"):
               row[1] = random.randint(0,100)
           print(row)

    with open('IoT_Sensor_Template/Light.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            print(row)

    with open('IoT_Sensor_Template/Pressure.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            print(row)

    with open('IoT_Sensor_Template/Prox.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            print(row)

    with open('IoT_Sensor_Template/Temp.csv') as f:
        reader = csv.reader(f)
        epoch_time = int(time.time())
        for row in reader:
            if (row[2] == "0"):
                row[2] = epoch_time
            if (row[1] == "0"):
                row[1] = random.randint(0, 100)
            print(row)