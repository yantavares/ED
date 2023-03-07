count = 0


def Fib(n):
    global count
    if n == 0:
        count += 1
        return 0
    elif n == 1:
        count += 1
        return 1
    else:
        count += 1
        return Fib(n-1) + Fib(n-2)


n = int(input())
print("Fib(%d) = %d (%d chamadas)" % (n, Fib(n), count))
