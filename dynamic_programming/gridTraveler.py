import datetime


def grid(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    elif m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        memo[(m, n)] = grid(m - 1, n, memo) + grid(m, n - 1, memo)
        return memo[(m, n)]


a = datetime.datetime.now()
print(grid(10, 4))
b = datetime.datetime.now()
print(b - a)
