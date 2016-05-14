class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        '''
        A public method
        '''

    def _internal_method(self):
        pass

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(Self):
        pass
    def public_method(self):
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1
    def __private_method(self):
        pass
