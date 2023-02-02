from space_invaders.engine.ioc.ioc import IoC, Register


class TestIocRegister:

    def test_success(self, mocker, scopes_test):
        scopes = scopes_test()
        mocker.patch.object(IoC, 'scopes', scopes)
        scopes.current_scope = mocker.PropertyMock()
        Register(key='test.key', func=print).execute()
        assert scopes.current_scope.__getattribute__('test.key')
        assert scopes.current_scope.__getattribute__('test.key') is print

    def test_call(self):
        Register(key='test.key', func=lambda x: x ** 2).execute()
        assert IoC.scopes.current_scope.__getattribute__('test.key')
        assert IoC.scopes.current_scope.__getattribute__('test.key')(7) == 49  # 7 ** 2
