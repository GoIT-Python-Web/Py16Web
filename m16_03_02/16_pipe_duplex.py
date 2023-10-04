from multiprocessing import Pipe, Process


class Foo:
    def __init__(self, value):
        self.value = value


def worker(receiver: Pipe):
    while True:
        try:
            instance = receiver.recv()
            receiver.send(f'Ok for: {instance}')
            print(f'Received: {instance}')
        except EOFError:
            return None


def wk(sender: Pipe, store):
    for el in store:
        sender.send(el)
        print(sender.recv())


def main():
    start_pipe, end_pipe = Pipe(duplex=True)
    foo = Foo(100)
    store = [12, 'Hello world', {'year': 2022}, foo, foo.value, 42, None, 43]
    my_worker = Process(target=worker, args=(end_pipe, ))
    my_wk = Process(target=wk, args=(start_pipe, store))
    my_worker.start()
    my_wk.start()

    my_wk.join()
    start_pipe.close()
    end_pipe.close()


if __name__ == '__main__':
    main()



