x = list(input())
aux = []
i = 0
while i < len(x):
    if x[i] == '*':
        x.pop(i)
        y = x.pop(i-1)
        aux.append(y)
        i = 0
    else:
        i += 1
print(*aux, sep="")
