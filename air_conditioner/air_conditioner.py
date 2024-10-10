class AirConditioner:

    def __init__(self, isOn: bool, temperature: int):
        self.isOn = isOn
        self.temperature = temperature

    def get_isOn(self):
        return self.isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def getTemperature(self):
        return self.temperature

    def setTemperature(self, temperature):
        self.temperature = temperature

    def increaseTemperature(self):
        self.temperature += 1

    def decreaseTemperature(self):
        self.temperature -= 1