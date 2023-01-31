import pytest

from space_invaders.engine.errors import exceptions
from space_invaders.engine.commands.change_angular_velocity import \
    ChangeAngularVelocity
from space_invaders.engine.interfaces import AngularVelocityController
from space_invaders.engine.interfaces.move import Vector
from space_invaders.tests.conftest import MockObj


def test_change_velocity(mock_obj):
    ChangeAngularVelocity(mock_obj).execute()
    assert mock_obj.angular_velocity == 1
    assert mock_obj.velocity == Vector(-14, 2)


@pytest.mark.skip('temporary skip')
def test_velocity_negative(mock_obj):
    mock_obj = MockObj(_velocity=Vector(2, -40), _direction=-30, _directions_number=-4)
    with pytest.raises(exceptions.NegativeAngularVelocityError):
        ChangeAngularVelocity(mock_obj).execute()
