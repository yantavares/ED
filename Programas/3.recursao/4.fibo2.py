def fibonacci(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    lst = fibonacci(n-1)
    return lst + [lst[-2]+lst[-1]]
