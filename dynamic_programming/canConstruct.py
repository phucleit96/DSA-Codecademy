def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canConstruct('eeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))