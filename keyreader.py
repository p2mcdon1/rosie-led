from buttonbase import ButtonBase
from pynput import keyboard


class KeyReader(ButtonBase):
    def __init__(self):

        self.__pressed = False

        def on_press(key):

            if key == keyboard.Key.esc:
                # kill the program
                quit()

            val = ''
            try:
                val = '{0}'.format(key.char)
            except AttributeError:
                print('special key {0} pressed'.format(
                    key))

            if (val == 'c'):
                self.__pressed = True

        # Collect events until released
        listener = keyboard.Listener(
            on_press=on_press)
        listener.start()

    def wasPressed(self):
        if self.__pressed:
            self.__pressed = False
            return True
        else:
            return False
