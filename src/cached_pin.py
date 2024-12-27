from machine import Pin

class CachedPin(Pin):
    '''
    Cached pin value.
    '''
    def __init__(self, pin_number, mode):
        super().__init__(pin_number, mode)
        self._value = None

    def on(self):
        '''
        Turn on the pin.
        :return:
        '''
        if self._value == 1:
            return
        super().on()
        self._value = 1

    def off(self):
        '''
        Turn off the pin.
        :return:
        '''
        if self._value == 0:
            return
        super().off()
        self._value = 0

    def value(self, val=None):
        if val is None:
            return
        else:
            if self._value == val:
                return
            super().value(val)
            self._value = val