from unittest.mock import Mock

import pytest

from space_invaders.engine.interfaces import Fuelable
from space_invaders.engine.interfaces.move import Movable, Vector
from space_invaders.engine.interfaces.rotate import Rotable


class MockObj(Mock, Movable, Rotable, Fuelable):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            self.__setattr__(k, v)

# Movable

    @property
    def position(self) -> Vector:
        return self._position

    @position.setter
    def position(self, vector: Vector) -> None:
        self._position = vector

    @property
    def velocity(self) -> Vector:
        return self._velocity

    @velocity.setter
    def velocity(self, value: Vector) -> None:
        self._velocity = value


# Rotable

    @property
    def direction(self) -> int:
        return self._direction

    @direction.setter
    def direction(self, direction: int) -> None:
        self._direction = direction

    @property
    def directions_number(self) -> int:
        return self._directions_number

    @property
    def angular_velocity(self) -> int:
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, velocity: int) -> None:
        self._angular_velocity = velocity

    @property
    def angular_velocity_correction(self) -> int:
        return self._angular_velocity_correction

    @angular_velocity_correction.setter
    def angular_velocity_correction(self, value: int) -> None:
        self._angular_velocity_correction = value


# Fuel

    @property
    def fuel(self) -> int:
        return self._fuel

    @fuel.setter
    def fuel(self, value: int) -> None:
        self._fuel = value

    @property
    def fuel_rate(self) -> int:
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value: int) -> None:
        self._fuel_rate = value


@pytest.fixture()
def mock_obj():
    return MockObj(
        _position=Vector(12, 5),
        _velocity=Vector(-7, 3),
        _angular_velocity=1,
        _directions_number=1,
        _direction=3,
        _fuel=10,
        _fuel_rate=1,
        _angular_velocity_correction=2
        )
