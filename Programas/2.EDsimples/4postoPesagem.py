n, f, p = map(int, input().split())
lst = list(map(int, input().split()))
tempo = 0
lst2 = []
count = f
while lst != []:
    for i in range(len(lst)):
        if count % f == 0:
            if lst[i] > p:
                tempo += 10
                lst2.append(lst[i]-2)

            else:
                tempo += 5
        else:
            tempo += 1
        count += 1
    lst[::] = lst2[::]
    lst2 = []
print(tempo)
