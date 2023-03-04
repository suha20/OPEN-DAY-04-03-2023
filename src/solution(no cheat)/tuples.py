# Introducing our first complex program in Python

a = (1, 2, 3)
b = (1, 2, 3)
# res = tuple(
#     [(a[i] + b[i]) for i in range(len(b))]
# )


# What about this quick cooking recipe?

def vector_add(a, b):
    result = [0] * len(a) ## cheat!
    n,N = 0, len(a)
    while n < N:
        result[n] = a[n] + b[n]
        n = n + 1
    return tuple(result)
