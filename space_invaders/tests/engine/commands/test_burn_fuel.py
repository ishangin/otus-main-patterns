import pytest

from space_invaders.engine.errors import exceptions
from space_invaders.engine.commands import BurnFuel
from space_invaders.engine.interfaces import Fuelable
from space_invaders.tests.utils import build_mock_object


@pytest.mark.parametrize(
    ('fuel', 'fuel_rate', 'expected_fuel_level'),
    [
        (10, 1, 9),
        (10, -1, 11),
        (10, 10, 0),
    ],
)
def test_burn_fuel_positive(fuel, fuel_rate, expected_fuel_level):
    mock = build_mock_object(
        Fuelable, fuel=fuel, fuel_rate=fuel_rate
    )
    BurnFuel(mock).execute()
    assert mock.fuel == expected_fuel_level


@pytest.mark.parametrize(
    ('fuel', 'fuel_rate', 'expected_exception'),
    [
        (1, 10, exceptions.NegativeFuelLevelError),
        (0, 1, exceptions.NegativeFuelLevelError),
    ],
)
def test_burn_fuel_negative(fuel, fuel_rate, expected_exception):
    mock = build_mock_object(
        Fuelable, fuel=fuel, fuel_rate=fuel_rate
    )
    with pytest.raises(expected_exception):
        BurnFuel(mock).execute()
