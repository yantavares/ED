def somalista(lst):
    if lst[1:] == []:
        print(lst[0])
    else:
        print(lst[0], "+", "soma("+str((lst[1:])) + ")")
    if len(lst) == 1:
        return lst[0]

    else:

        return lst[0] + somalista(lst[1:])


def geraImpar(n):
    end = []
    i = 1
    for k in range(n):
        end.append(i)
        i += 2
    return end


n = int(input())
impares = geraImpar(n)
x = somalista(impares)
print("---------------")
print("%d ** 2 ==" % x**(0.5), x)
