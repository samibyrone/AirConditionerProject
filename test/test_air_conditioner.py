import unittest

from air_conditioner.air_conditioner import AirConditioner


class TestAirConditioner(unittest.TestCase):

    def test_new_air_conditioner_to_be_turnOff(self):
        air_conditioner = AirConditioner()
        self.assertFalse(air_conditioner.turnOff())

    def test_new_air_conditioner_that_can_be_turnOn(self):
        air_conditioner = AirConditioner()
        self.assertFalse(air_conditioner.turnOff())
        my_air_conditioner = air_conditioner.turnOn()
        self.assertEqual(air_conditioner.turnOn(), my_air_conditioner)

    def test_new_air_conditioner_can_be_turn_on_and_increase_temperature(self):
        air_conditioner = AirConditioner()
        air_conditioner.turnOn()
        air_conditioner.increaseTemperature()
        self.assertEqual(air_conditioner.getTemperature(), 17)

    def test_new_air_conditioner_can_be_turn_on_and_decrease_temperature(self):
        air_conditioner = AirConditioner()
        air_conditioner.turnOn()
        air_conditioner.decreaseTemperature()
        self.assertEqual(air_conditioner.getTemperature(), 15)

    def test_new_air_conditioner_can_be_turn_on_and_temperature_increase_up_to_30C(self):
        air_conditioner = AirConditioner()
        air_conditioner.turnOn()
        air_conditioner.setTemperature(30)
        self.assertEqual(air_conditioner.getTemperature(), 30, "Temperature should be set correctly")

    def test_new_air_conditioner_can_be_turn_on_and_temperature_decrease_not_below_16C(self):
        air_conditioner = AirConditioner()
        air_conditioner.turnOn()
        air_conditioner.setTemperature(16)
        self.assertEqual(air_conditioner.getTemperature(), 16, "Temperature should be set correctly")