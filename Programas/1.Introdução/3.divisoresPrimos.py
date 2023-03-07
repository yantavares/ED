def divisores(n):
    end = []
    for k in range(1, n//2 + 1):
        if n % k == 0:
            end.append(k)

    end.append(n)
    return end
