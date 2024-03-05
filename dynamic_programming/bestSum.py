def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = targetSum - num
        remainder_result = bestSum(remainder, numbers, memo)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[targetSum] = shortest_combination
    return shortest_combination

print(bestSum(8, [4, 2, 5, 3]))
print(bestSum(100, [1, 2, 5, 25]))
print(bestSum(100, [7, 17]))

