n = int(input())

amigosMussum = input().split()
amigosMussum.pop(0)
amigosMussum.pop(0)

candidatis = {}

for k in range(n-1):
    inst = input().split()
    inst.pop(1)
    nome = inst[0]
    candidatis[inst[0]] = []
    inst.pop(0)
    for l in inst:
        if nome not in amigosMussum:
            candidatis[nome].append(l)
        else:
            break
end = []
count = 0
for k in candidatis:
    count = 0
    for i in candidatis[k]:
        if i in amigosMussum:
            count += 1
            if count >= 3:
                end.append(k)
                break

if end == []:
    print("Cacildis! Cade elis?")
else:
    end = sorted(end)

for i in end:
    print(i)