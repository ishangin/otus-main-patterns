import threading
from typing import TypeVar

from space_invaders.engine.errors.exceptions import IocResolveException
from space_invaders.engine.interfaces import Command

T = TypeVar('T')


class ScopeNew(Command):
    def __init__(self, scopes: object, parent: int):
        self._scopes = scopes
        self._parent = parent

    def execute(self) -> None:
        self._scopes.new_scope(parent=self._parent)


class ScopeSetCurrent(Command):
    def __init__(self, scopes: object, scope: int):
        self._scopes = scopes
        self._scope = scope

    def execute(self) -> None:
        self._scopes.current_scope = self._scope


class Scopes(threading.local):

    class _Scope:
        def __init__(self, index: int, parent: int | None):
            self.parent = parent
            self.id = index

    def __init__(self):
        super().__init__()
        root_scope = self._Scope(index=0, parent=None)  # create root scope
        root_scope.__setattr__('IoC.Register', Register)
        root_scope.__setattr__('Scope.New', ScopeNew)
        root_scope.__setattr__('Scope.SetCurrent', ScopeSetCurrent)
        self.value: dict = {0: root_scope}  # set root scope
        self._max_scope_id: int = 0
        self._cur_scope: int = 0

    @property
    def current_scope(self) -> _Scope:
        return self.value[self._cur_scope]

    @current_scope.setter
    def current_scope(self, index: int) -> None:
        self._cur_scope = index

    def new_scope(self, parent: int | None):
        self._max_scope_id += 1
        new_scope = self._Scope(index=self._max_scope_id, parent=parent)
        self.value.update({self._max_scope_id: new_scope})
        self._cur_scope = self._max_scope_id


class Register(Command):
    def __init__(self, key: str, func: callable):
        self._key = key
        self._func = func

    def execute(self) -> None:
        IoC.scopes.current_scope.__setattr__(self._key, self._func)


class IoC:

    scopes = Scopes()

    @staticmethod
    def resolve(key: str, *args) -> T:
        scope = IoC.scopes.current_scope
        call = None
        try:
            while not call:
                try:
                    call = scope.__getattribute__(key)(*args)
                except AttributeError:
                    scope = IoC.scopes.value[scope.parent]
        except KeyError:
            raise IocResolveException(f'unresolved registration {key}')

        return call
