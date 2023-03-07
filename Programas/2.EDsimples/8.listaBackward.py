end = []
count = 0
while True:
    x = input().split(" ")
    if x[0] == 'f':
        break
    if x[0] == 'i':
        if x[2] == '0' or int(x[2]) > len(end):
            end.append([int(x[1]), count])
        else:
            pos = len(end) - int(x[2])
            end.append([int(x[1]), count, pos])
    count += 1
    if x[0] == 'r':

        temp = -2
        k = 0
        while k < len(end):
            if end[k][0] == int(x[1]):
                temp = end[k]
            if len(end[k]) > 2:
                if end.index(temp) == end[k][2]:
                    end[k].pop(2)
            if temp != -2 and len(end[k]) > 2:
                if end[k][2] > end.index(temp):
                    end[k][2] = end[k][2] - 1
            k += 1
        if temp != -2:
            end.remove(temp)
if end == []:
    print(-1)
else:
    fim = ''
    for n in end:
        fim += str(n)
    fim = fim.replace(" ", "")
    fim = fim.replace("][", "] [")

    print(fim)
