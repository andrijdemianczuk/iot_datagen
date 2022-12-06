from entities import sHumidity, sProx, sTemp, sLight, sPressure

if __name__ == '__main__':

    runType = "file"

    if runType == "file":
        sHumidity.Humidity("temp/", "IoT_Sensor_Template/").run()
        sProx.Prox("temp/", "IoT_Sensor_Template/").run()
        sTemp.Temp("temp/", "IoT_Sensor_Template/").run()
        sLight.Light("temp/", "IoT_Sensor_Template/").run()
        sPressure.Pressure("temp/", "IoT_Sensor_Template/").run()

    if runType == "kafka":
        # topic and bootstrap servers should be configured as yaml file parameters
        sHumidity.KHumidity(topic="dev1", bootstrap_servers=['35.86.112.176:9092']).run() #topic name should be something like 'building_iot_humidity'

    if runType == "":
        pass
