from animation import Animation


class Mouse(Animation):
    # override
    def run(self, runFlag):
        print('starting to run Mouse...')
        while runFlag():
            print('Mouse is running...')
            self.rest()

        print('done running Mouse')
