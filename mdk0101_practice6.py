def sizer(cls):
    class Sized(cls):
        @property
        def size(self):
            if hasattr(self, '__len__') and callable(getattr(self, '__len__')):
                return len(self)
            elif hasattr(self, '__abs__') and callable(getattr(self, '__abs__')):
                return abs(self)
            else:
                return 0