t, n = map(int, input().split())
x = []
lst = []
end = []
end2 = []
if n != 0:
    x = list(map(int, input().split(" ")))


count = list(range(t))

for i in x:
    mod = i % t
    if mod in count:
        end.append([mod, i])

for i in count:
    for n in end:
        if n[0] == i:
            end2.append(n)

resp = {}
for i in range(t):
    resp.setdefault(i, [])
for i in end2:
    if i[0] in resp:
        resp[i[0]].append(i[1])
for i, value in resp.items():
    print(i, end=' - ')
    if resp[i] == []:
        print('[x]')
    else:
        print(*value, sep=' -> ')
