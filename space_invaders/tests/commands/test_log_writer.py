import pytest
from unittest.mock import Mock

from space_invaders.engine.commands.log_writer import LogWriter, log


class TestLogWriter:
    def test_success(self):
        log.exception = Mock()
        exc = ValueError('Some exception')

        try:
            raise exc
        except ValueError:
            LogWriter(exc).execute()

        log.exception.assert_called_once_with(exc)

    def test_fail(self):
        log.exception = Mock()
        log.exception.side_effect = AttributeError('Some went wrong')
        exc = AttributeError('Some exception')

        try:
            raise exc
        except AttributeError:
            with pytest.raises(AttributeError):
                LogWriter(exc).execute()

        log.exception.assert_called_once_with(exc)
