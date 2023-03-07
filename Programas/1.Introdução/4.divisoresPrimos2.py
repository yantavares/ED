import math


def ePrimo(n):

    x = 2
    end = 0

    if n > 1:
        while x <= (math.sqrt(n) // 1):
            if n % x == 0:
                end = 1
                break
            else:
                end = 0

            x += 1
    else:
        end = 1

    return end


def primos_gemeos(n):
    final = []
    count = 0
    inicio = 2
    end = []
    while count < n:
        while len(end) < 2:
            if ePrimo(inicio) == 0:
                end.append(inicio)
            inicio += 1
        if end[1] == end[0] + 2:
            temp = (end[0], end[1])
            final.append(temp)
            temp = ()
            count += 1
        del end[0]

    return final
