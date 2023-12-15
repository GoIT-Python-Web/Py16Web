def knapSack(W: int, wt: list, val: list, n: int) -> int:

    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    # print(K)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 and w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    for i in range(n + 1):
        print(K[i])
    return K[n][W]


if __name__ == '__main__':

    value = [60, 100, 120]
    weight = [10, 20, 30]

    capacity = 50

    n = len(value)

    print(knapSack(capacity, weight, value, n))
