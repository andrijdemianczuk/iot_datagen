from entities import sHumidity, sProx, sTemp, sLight, sPressure

if __name__ == '__main__':
    #TODO: Refactor the objects as a duck type later
    sHumidity.Humidity("IoT_Sensor_Template/", "temp/").run()
    sProx.Prox("IoT_Sensor_Template/", "temp/").run()
    sTemp.Temp("IoT_Sensor_Template/", "temp/").run()
    sLight.Light("IoT_Sensor_Template/", "temp/").run()
    sPressure.Pressure("IoT_Sensor_Template/", "temp/").run()
