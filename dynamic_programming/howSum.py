def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]
    memo[targetSum] = None
    return None


print(howSum(14, [3, 6, 5]))