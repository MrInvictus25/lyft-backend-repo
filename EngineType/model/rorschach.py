from datetime import datetime

from EngineType.Engine.willoughby_engine import WilloughbyEngine
from EngineType.Battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car

class Rorschach(WilloughbyEngine, NubbinBattery):
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tires)
        return car
