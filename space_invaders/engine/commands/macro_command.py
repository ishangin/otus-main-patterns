import logging
from typing import TypeVar

from space_invaders.engine.commands import BurnFuel, Rotate
from space_invaders.engine.commands.change_angular_velocity import ChangeAngularVelocity
from space_invaders.engine.commands.check_fuel import CheckFuel
from space_invaders.engine.commands.move import Move
from space_invaders.engine.errors.exceptions import CommandException
from space_invaders.engine.interfaces import Command, Fuelable
from space_invaders.engine.interfaces.move import Movable
from space_invaders.engine.interfaces.rotate import Rotable

log = logging.getLogger(__name__)

MF = TypeVar('MF', Movable, Fuelable)
MRF = TypeVar('MRF', Movable, Rotable, Fuelable)


class MacroCommand(Command):

    def __init__(self, commands: list[Command]):
        self._commands = commands

    def execute(self):
        try:
            for command in self._commands:
                command.execute()
        except CommandException as exc:
            log.error(exc)
            raise


class Movement(MacroCommand):
    commands = [CheckFuel, Move, BurnFuel]

    def __init__(self, obj: MF):
        super().__init__([command(obj) for command in self.commands])


class Rotatement(MacroCommand):
    commands = [CheckFuel, Rotate, BurnFuel, ChangeAngularVelocity]

    def __init__(self, obj: MRF):
        super().__init__([command(obj) for command in self.commands])
