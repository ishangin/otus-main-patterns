import pytest

from space_invaders.engine.errors.exceptions import IocResolveException
from space_invaders.engine.ioc.ioc import IoC


class TestIoC:
    """ tests for IoC class"""

    def test_ioc(self):
        class TestClass:
            ...

        assert hasattr(IoC, 'resolve')
        IoC.resolve('IoC.Register', 'A', TestClass).execute()
        assert isinstance(IoC.resolve('A'), TestClass)

    def test_ioc_unresolved_dependency(self):
        with pytest.raises(IocResolveException):
            IoC.resolve('Unresolved.Dependency', 'args').execute()
