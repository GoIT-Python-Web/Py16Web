from multiprocessing import Pool


def worker(val):
    return val ** 2


if __name__ == '__main__':

    with Pool(2) as pool:
        r = pool.map(worker, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(r)

        iterator = pool.imap(worker, range(10))
        print(iterator)
        print(iterator.next())
        [print(el, end=" ") for el in iterator]
