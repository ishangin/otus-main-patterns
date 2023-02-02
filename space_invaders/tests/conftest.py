import pytest


class ScopesTest:

    def new_scope(self):
        ...

    def current_scope(self):
        ...


@pytest.fixture()
def scopes_test():
    return ScopesTest
