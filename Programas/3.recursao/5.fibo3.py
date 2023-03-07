lst = []


def fibonacci(n):
    global lst
    if n == 0:
        lst.append(n)
        return 0
    elif n == 1:
        lst.append(n)
        return 1
    else:
        lst.append(n)
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input())

print("fibonacci(%d) = %d." % (n, fibonacci(n)))
for i in range(n+1):
    count = 0
    for k in lst:
        if k == i:
            count += 1
    print("%d chamada(s) a fibonacci(%d)." % (count, i))
