graf1 = []
graf2 = []

n = int(input())

for k in range(n):
    inst = list(map(int,input().split()))
    prim = inst.pop(0)
    tam = inst.pop(0)
    for j in range(tam):
        graf1.append((prim, inst[j]))

inutil = input()
n = int(input())

for k in range(n):
    inst = list(map(int,input().split()))
    prim = inst.pop(0)
    tam = inst.pop(0)
    for j in range(tam):
        graf2.append((prim, inst[j]))

deuBom = True
for i in graf2:
    if i not in graf1:
        print('Ue? Ue? Ue?')
        deuBom = False
        break
if deuBom == True:
    print('Sub-sub!')
