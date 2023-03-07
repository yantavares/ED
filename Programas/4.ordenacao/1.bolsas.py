n = int(input())
notas = []
for i in range(n):
    k = float(input())
    notas.append(k)

notas = sorted(notas, reverse=True)

for j in notas:
    print("%.2f" % (j))
