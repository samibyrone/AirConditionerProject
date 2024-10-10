class AirConditioner:

    def __init__(self):
        self.isOn = bool
        self.temperature = 16

    def get_isOn(self):
        return self.isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def increaseTemperature(self):
        self.temperature += 1

    def decreaseTemperature(self):
        self.temperature -= 1

    def getTemperature(self):
        if self.temperature <= 16:
            self.isOn = True
            print("You can not Decrease the Temperature Below 16`C")
        return self.temperature

    def setTemperature(self, temperature):
        if temperature >= 30:
            self.isOn = True
            print("You can not Increase Temperature more than 30`C")
        self.temperature = temperature

