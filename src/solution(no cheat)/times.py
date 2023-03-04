# Plan
#    res = tuple([(i, num, i * num) for i in range(1, 11)])
#    return res
# Explain how we get access to minus 1.
def time_tables(num):
    res = [(0, 0, 0)] * 10
    n = 0
    while n < 10:
        res[n] = (n+1,num, (n+1) * num)
        n = n + 1
    return tuple(res)
