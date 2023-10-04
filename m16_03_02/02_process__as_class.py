import sys
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        self.kwargs.get('log')(f"args: {self.args}")
        sys.exit(0)


def log(msg):
    print(msg)


if __name__ == '__main__':
    for i in range(5):
        pr = MyProcess(args=(f"Count Process - {i}",), kwargs={'log': log})
        pr.start()
