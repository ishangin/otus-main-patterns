from unittest.mock import patch

import pytest

from space_invaders.engine.commands import Rotate, BurnFuel
from space_invaders.engine.commands.change_angular_velocity import ChangeAngularVelocity
from space_invaders.engine.commands.change_linear_velocity import ChangeLinearVelocity
from space_invaders.engine.commands.check_fuel import CheckFuel
from space_invaders.engine.commands.macro_command import MacroCommand, Movement, \
    Rotatement
from space_invaders.engine.commands.move import Move
from space_invaders.engine.errors.exceptions import CommandException
from space_invaders.engine.interfaces import Fuelable, Command
from space_invaders.engine.interfaces.move import Movable, Vector
from space_invaders.engine.interfaces.rotate import Rotable
from space_invaders.tests.conftest import MockObj


class TestMacroCommand:

    def test_success(self, mock_obj):

        with \
                patch.object(Move, 'execute'),\
                patch.object(Rotate, 'execute'), \
                patch.object(CheckFuel, 'execute'), \
                patch.object(BurnFuel, 'execute'):

            commands = [Move, Rotate, CheckFuel, BurnFuel]

            MacroCommand([command(mock_obj) for command in commands]).execute()

            Move.execute.assert_called()
            Rotate.execute.assert_called()
            CheckFuel.execute.assert_called()
            BurnFuel.execute.assert_called()

    def test_fail_raise_exception(self):

        class FakeCmd(Command):
            pass

        with pytest.raises(TypeError):
            MacroCommand([FakeCmd()]).execute()

    def test_success_movement(self, mock_obj):
        with \
                patch.object(Move, 'execute'),\
                patch.object(CheckFuel, 'execute'), \
                patch.object(BurnFuel, 'execute'):

            Movement(mock_obj).execute()

            for command in Movement.commands:
                command.execute.assert_called()

    def test_success_movement_values(self, mock_obj):

        Movement(mock_obj).execute()

        assert mock_obj.position == Vector(5, 8)
        assert mock_obj.fuel == 9

    def test_fail_movement(self):
        mock_obj = MockObj(_fuel=1, _fuel_rate=10)
        with pytest.raises(CommandException):
            Movement(mock_obj).execute()

    def test_success_rotatement(self, mock_obj):
        with \
                patch.object(CheckFuel, 'execute'), \
                patch.object(Rotate, 'execute'), \
                patch.object(BurnFuel, 'execute'), \
                patch.object(ChangeAngularVelocity, 'execute'):

            Rotatement(mock_obj).execute()

            for command in Rotatement.commands:
                command.execute.assert_called()

    def test_success_rotatement_values(self, mock_obj):

        movable_obj = MockObj(
                _position=Vector(10, 10),
                _velocity=Vector(2, -4),
                _fuel=10,
                _fuel_rate=2,
                _direction=1,
                _directions_number=8,
                _angular_velocity=3
            )

        Rotatement(movable_obj).execute()

        assert movable_obj.position == Vector(10, 10)
        assert movable_obj.fuel == 8
        assert movable_obj.velocity == Vector(0, -4)

    def test_fail_rotatement(self):

        mock_obj = MockObj(_fuel=1, _fuel_rate=10)

        with pytest.raises(CommandException):
            Rotatement(mock_obj).execute()
