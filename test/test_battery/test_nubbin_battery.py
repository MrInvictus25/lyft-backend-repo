import unittest
from datetime import datetime
from datetime import date

from EngineType.Battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-05-06")
        last_service_date = date.fromisoformat("2019-04-06")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-05-06")
        last_service_date = date.fromisoformat("2022-05-06")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
