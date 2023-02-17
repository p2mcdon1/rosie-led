class ThreaderBase:
    def startAnimation(self, run, checkRun):
        def func(): return self.__animate(run, checkRun)
        self.startAnimationThread(func)

    def acquireLock(self):
        pass

    def releaseLock(self):
        pass

    def __animate(self, run, checkRun):
        self.acquireLock()
        run(checkRun)
        self.releaseLock()

    def startAnimationThread(self, func):
        pass
