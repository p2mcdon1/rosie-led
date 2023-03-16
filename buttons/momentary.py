from buttons.buttonbase import ButtonBase
from machine import Pin
from parms import Parms


class Momentary(ButtonBase):
    def __init__(self):

        self.__pressed = False
        parms = Parms()
        pin = Pin(parms.momentarySwitchPin, Pin.IN, Pin.PULL_UP)

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
