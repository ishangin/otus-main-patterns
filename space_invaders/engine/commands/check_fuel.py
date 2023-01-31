from space_invaders.engine.errors.exceptions import CommandException
from space_invaders.engine.interfaces import Command, Fuelable


class CheckFuel(Command):
    def __init__(self, f: Fuelable):
        self._f = f

    def execute(self):
        if self._f.fuel >= self._f.fuel_rate:
            return None
        else:
            raise CommandException('low fuel')
