from multiprocessing import Process
from multiprocessing.dummy import Pool  # Thread с оболочкой Process
from threading import Thread
from time import time


def worker(values, filename):
    with open(filename, 'a') as f:
        for num in values:
            f.write(f'{num ** 2}\n')


if __name__ == '__main__':
    values = list(range(600_000))

    th_filename = 'th_squares.txt'
    threads = [
        Thread(target=worker, args=(values[:200_000], th_filename)),
        Thread(target=worker, args=(values[200_000:400_000], th_filename)),
        Thread(target=worker, args=(values[400_000:], th_filename)),
    ]
    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Done by 3 threads: {round(time() - timer, 4)}')

    pr_filename = 'pr_squares.txt'
    processes = [
        Process(target=worker, args=(values[:200_000], pr_filename)),
        Process(target=worker, args=(values[200_000:400_000], pr_filename)),
        Process(target=worker, args=(values[400_000:], pr_filename)),
    ]

    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    [process.close() for process in processes]
    print(f'Done by 3 processes: {round(time() - timer, 4)}')

    timer = time()
    worker(values, 'squares.txt')
    print(f'Done by 1 process: {round(time() - timer, 4)}')

    pl_filename = 'pl_squares.txt'
    timer = time()
    with Pool(3) as pool:
        result = pool.starmap(worker, [(values[:200_000], pl_filename),
                                       (values[200_000:400_000], pl_filename),
                                       (values[400_000:], pl_filename)])
    print(f'Done by 3 pool processes dummy: {round(time() - timer, 4)}')
