import datetime
def fib(n, memo=None):
    if memo is None:
        memo = {}
    answer = None
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        answer = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = answer
        return answer

def fib_dp(n):
    if n <= 1:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1]

a= datetime.datetime.now()
print(fib(40))
b = datetime.datetime.now()
print(b-a)
c = datetime.datetime.now()
print(fib_dp(40))
d = datetime.datetime.now()
print(d-c)
