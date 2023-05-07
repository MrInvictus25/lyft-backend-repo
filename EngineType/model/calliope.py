from datetime import datetime
from EngineType.Engine.capulet_engine import CapuletEngine
from EngineType.Battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car
class Calliope():
    def model_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car
