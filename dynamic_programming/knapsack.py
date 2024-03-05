def knapSack(weights, values, W, n):
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        return knapSack(weights, values, W, n-1)
    else:
        include = values[n-1] + knapSack(weights, values, W-weights[n-1], n-1)
        exclude = knapSack(weights, values, W, n-1)
        return max(include, exclude)

def knapSackDP(weights, values, W, n, memo=None):
    if memo is None:
        memo = {}
    if (n, W) in memo:
        return memo[(n, W)]
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        memo[(n, W)] = knapSackDP(weights, values, W, n-1, memo)
        return memo[(n, W)]
    else:
        include = values[n-1] + knapSackDP(weights, values, W-weights[n-1], n-1, memo)
        exclude = knapSackDP(weights, values, W, n-1, memo)
        memo[(n, W)] = max(include, exclude)
        return memo[(n, W)]

weights = [10, 20, 30]
values = [60, 100, 120]
W = 50
n = len(weights)
print(knapSack(weights, values, W, n))
