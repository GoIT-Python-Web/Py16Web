from multiprocessing import Process, Event
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        if event_for_exit.is_set():
            continue
        else:
            print('Run event work')


if __name__ == '__main__':
    event = Event()
    pr = Process(target=example_work, args=(event,), daemon=True)
    pr.start()
    print('Start!')
    sleep(3)
    print('Stop!')
    event.set()
    sleep(3)
    print('Start!')
    event.clear()
    sleep(3)
    print('Stop!')
    event.set()
    print('End program')
