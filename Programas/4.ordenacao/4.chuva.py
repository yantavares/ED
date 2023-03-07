import math
n = int(input())
notas = []
for i in range(n):
    p, c = map(int, input().split())
    try:
        notas.append((p, c, math.ceil(c/p)))
    except:
        if c != 0:
            notas.append((0, 0, 0))
        else:
            notas.append((p, c, c))

temp = sorted(notas, key=lambda notas: notas[0])
end = sorted(temp, key=lambda temp: temp[2], reverse=True)

for i in end:
    print("%d / %d" % (i[2], i[0]))
