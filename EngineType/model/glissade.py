from datetime import datetime
from EngineType.Engine.willoughby_engine import WilloughbyEngine
from EngineType.Battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car

class Glissade():
    def model_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tires)
        return car
