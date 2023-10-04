from multiprocessing import Process, RLock as PRLock
from multiprocessing.dummy import Pool, RLock as DummyLock  # Thread с оболочкой Process
from threading import Thread, RLock as TRlock
from time import time


def worker(values, filename, lock):
    with lock:
        with open(filename, 'a') as f:
            for num in values:
                f.write(f'{num ** 2}\n')


if __name__ == '__main__':
    values = list(range(600000))
    th_lock = TRlock()
    th_filename = 'th_squares.txt'
    threads = [
        Thread(target=worker, args=(values[:200000], th_filename, th_lock)),
        Thread(target=worker, args=(values[200000:400000], th_filename, th_lock)),
        Thread(target=worker, args=(values[400000:], th_filename, th_lock)),
    ]
    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Done by 3 threads: {round(time() - timer, 4)}')

    pr_filename = 'pr_squares.txt'
    p_lock = PRLock()
    processes = [
        Process(target=worker, args=(values[:200000], pr_filename, p_lock)),
        Process(target=worker, args=(values[200000:400000], pr_filename, p_lock)),
        Process(target=worker, args=(values[400000:], pr_filename, p_lock)),
    ]

    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    [process.close() for process in processes]
    print(f'Done by 3 processes: {round(time() - timer, 4)}')

    timer = time()
    worker(values, 'squares.txt', th_lock)
    print(f'Done by 1 process: {round(time() - timer, 4)}')

    pl_filename = 'pl_squares.txt'
    timer = time()
    dummy_lock = DummyLock()
    with Pool(3) as pool:
        result = pool.starmap(worker,
                              [(values[:200000], pl_filename, dummy_lock),
                               (values[200000:400000], pl_filename, dummy_lock),
                               (values[400000:], pl_filename, dummy_lock)])
    print(f'Done by 3 pool processes dummy: {round(time() - timer, 4)}')
