from entities import sHumidity, sProx, sTemp, sLight, sPressure

if __name__ == '__main__':
    sHumidity.Humidity("temp/", "IoT_Sensor_Template/").run()
    sProx.Prox("temp/", "IoT_Sensor_Template/").run()
    sTemp.Temp("temp/", "IoT_Sensor_Template/").run()
    sLight.Light("temp/", "IoT_Sensor_Template/").run()
    sPressure.Pressure("temp/", "IoT_Sensor_Template/").run()
