def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = allConstruct(suffix, wordBank, memo)
            target_ways = list(map(lambda x: [word] + x, suffix_ways))
            result.extend(target_ways)
    memo[target] = result
    return result

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))