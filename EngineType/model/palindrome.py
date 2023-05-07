from datetime import datetime

from EngineType.Engine.sternman_engine import SternmanEngine
from EngineType.Battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car

class Palindrome(SternmanEngine, SpindlerBattery):
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car
