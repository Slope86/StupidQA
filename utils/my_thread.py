import threading


# Thread with target function return valve
class MyThread(threading.Thread):
    def __init__(self, target=None, args=(), **kwargs):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        if self._target is None:
            return
        self.__result__ = self._target(*self._args, **self._kwargs)

    def result(self):
        self.join()
        return self.__result__
