'''
Recursivo:

k = int(input())
for i in range(k):
    n = int(input())

    def fat(n):
        if n == 1:
            print(1, end=" ")
            return 1
        else:
            x = (n * fat(n-1)) % 2357
            print(x, end=" ")
            return x

    print(1, end=" ")
    fat(n)
    print("")
'''


def fat(n):
    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult % 2357


it = int(input())
for j in range(it):
    n = int(input())
    for k in range(n):
        print(fat(k), end=" ")
    print(fat(n))
