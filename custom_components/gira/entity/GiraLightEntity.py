from homeassistant.components.light import LightEntity
from .GiraEntity import GiraEntity

class GiraLightEntity(LightEntity, GiraEntity):
    @staticmethod
    def create(device):
        return GiraLightEntity(device)

    def __init__(self, device):
        self.device = device
        self._value = int(self.device.getState())
        self._name = " ".join(self.device.getName().split("\\")[1:])
        self._id = self.device.getId()

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._id

    @property
    def is_on(self):
        return self._value == 1

    def update(self):
        pass

    def turn_on(self, **kwargs):
        self._value = 1
        self.device.turnOn()

    def turn_off(self, **kwargs):
        self._value = 0
        self.device.turnOff()