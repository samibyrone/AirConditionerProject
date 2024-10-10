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
        self.assertEqual(air_conditioner.increaseTemperature(), air_conditioner.temperature)