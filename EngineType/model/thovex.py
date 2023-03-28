from datetime import datetime

from EngineType.Engine.capulet_engine import CapuletEngine
from EngineType.Battery.nubbin_battery import NubbinBattery


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
