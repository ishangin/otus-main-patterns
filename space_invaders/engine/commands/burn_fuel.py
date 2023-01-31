from space_invaders.engine.errors import exceptions
from space_invaders.engine.interfaces import Command, Fuelable


class BurnFuel(Command):
    """Выполнить изменение уровня топлива.

    Args:
        obj: Объект, для которого выполняется изменение уровня топлива.
    """

    def __init__(self, obj: Fuelable):
        self.obj = obj

    def execute(self) -> None:
        level = self.obj.fuel - self.obj.fuel_rate
        if level < 0:
            raise exceptions.NegativeFuelLevelError
        self.obj.fuel = level
