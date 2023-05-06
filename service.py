from abc import ABC, abstractmethod


class ServiceInfo(ABC):
    @abstractmethod
    def needs_service(self):
        pass
