from machine import Pin

class CachedPin(Pin):
    '''
    Cached pin value.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = None

    def value(self, val=None):
        if val is None or self._value == val:
            return
        super().value(val)
        self._value = val