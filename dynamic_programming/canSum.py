def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainders = targetSum - num
        if canSum(remainders, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(8, [2, 4, 13]))
