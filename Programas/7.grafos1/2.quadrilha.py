num = int(input())
pal = {}
for k in range(num):
    inst = input().split()
    conexoes = inst[2:]
    pal[inst[0]] = conexoes

vistos = []

def travessia(k):
    if k in vistos:
        return False

    vistos.append(k)

    for l in pal[k]:
        if l in vistos and l != vistos[-1]:
            return True
        else:
            travessia(l)
    

deuBom = False
for no in pal:
    if travessia(no) == True:
        print('Hoje tem!')
        deuBom = True
        break

if not deuBom:
    print('... que ama ninguem.')