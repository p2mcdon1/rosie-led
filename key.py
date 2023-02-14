from machine import Pin


class KeyReader:
    def __init__(self):

        self.pushed = False

        pin = Pin(4, Pin.IN, Pin.PULL_UP)

        def button_callback(p):
            if not self.pushed and pin.value() == 0:
                self.pushed = True

        pin.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

    def wasPushed(self):
        if self.pushed:
            self.pushed = False
            return True
        else:
            return False
