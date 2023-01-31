from abc import ABC, abstractmethod


class Fuelable(ABC):
    """Объект, обладающий свойством изменения уровня топлива."""

    @property
    @abstractmethod
    def fuel(self) -> int:
        """Уровень топлива."""

    @fuel.setter
    @abstractmethod
    def fuel(self, value: int) -> None:
        """Уровень топлива."""

    @property
    @abstractmethod
    def fuel_rate(self) -> int:
        """Расход топлива."""

    @fuel_rate.setter
    @abstractmethod
    def fuel_rate(self, value: int) -> int:
        """Расход топлива."""
