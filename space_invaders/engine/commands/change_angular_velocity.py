from math import cos, pi, sin

from space_invaders.engine.errors import exceptions
from space_invaders.engine.interfaces import AngularVelocityController, Command
from space_invaders.engine.interfaces.move import Vector, Movable


class ChangeAngularVelocity(Command):
    """Команда изменения угловой скорости"""

    def __init__(self, obj: Movable | AngularVelocityController):
        self._obj = obj

    def execute(self) -> None:
        if self._obj.velocity != Vector(0, 0):  # if object is moving
            d = self._obj.direction
            n = self._obj.directions_number
            v = self._obj.velocity

            # rounded 1e-5
            self._obj.velocity = Vector(x=int(v.x + v.x * cos((2 * pi * d) / n)),
                                        y=int(v.y + v.y * sin((2 * pi * d) / n)))
