n = input()
roupas = input().split()
roupaVista = set()
dups = [x for x in roupas if x in roupaVista or roupaVista.add(x)]

print(len(dups))
