n = int(input())
for i in range(n):
    s = input()
    s = list(s)
    s = list(map(int, s))

    while len(s) > 1:
        if s[0] == 0:
            s.pop(0)
        else:
            break

    while len(s) > 1:
        if s[-1] == 0:
            s.pop(-1)
        else:
            break

    if s[0] == 0:
        print(0)

    else:
        count = 0
        for i in s:
            if i == 0:
                count += 1

        print(count)
