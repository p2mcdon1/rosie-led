from pynput import keyboard
import queue

class KeyReader:
    def __init__(self):

        self.keyQueue = queue.Queue()

        def on_press(key):
            try:
                # queue the string representation
                self.keyQueue.put('{0}'.format(key.char))
            except AttributeError:
                print('special key {0} pressed'.format(
                    key))

        def on_release(key):
            if key == keyboard.Key.esc:
                # queue the key
                self.keyQueue.put(self.stop())

                # Stop listener
                return False

        # Collect events until released
        listener = keyboard.Listener(
                on_press=on_press,
                on_release=on_release)
        listener.start()

    def stop(self):
        return '##QUIT##'
