n = int(input())
notas = []
for i in range(n):
    k = float(input())
    notas.append(k)

notas = sorted(notas)

print("%.2f" % notas[0])
print("%.2f" % notas[len(notas)//2])
print("%.2f" % notas[-1])