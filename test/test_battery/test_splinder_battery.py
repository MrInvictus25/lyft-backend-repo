import unittest
from datetime import date

from EngineType.Battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-05-06")
        last_service_date = date.fromisoformat("2020-04-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-05-06")
        last_service_date = date.fromisoformat("2023-02-06")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
