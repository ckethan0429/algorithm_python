import itertools
itertools.permutations
def dp(x):
    d = []

    if x == 1 :
        return 1
    if x == 2 :
        return 1
    if d[x] is not None:
        return d[x] 
    return d.append(dp(x-1) + dp(x-2))

print(dp(10))

