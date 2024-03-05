def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
        if target in memo:
            return memo[target]
    if target == "":
        return 1
    total_count = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            no_ways = countConstruct(suffix, wordBank, memo)
            total_count += no_ways

    memo[target] = total_count
    return total_count
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

