from buttonbase import ButtonBase
from machine import Pin


class MomentarySwitch(ButtonBase):
    def __init__(self):

        self.__pressed = False

        pin = Pin(4, Pin.IN, Pin.PULL_UP)

        def button_callback(p):
            if not self.__pressed and pin.value() == 0:
                self.__pressed = True

        pin.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

    def wasPressed(self):
        if self.__pressed:
            self.__pressed = False
            return True
        else:
            return False
