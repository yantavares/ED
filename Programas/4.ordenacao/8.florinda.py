pretendentes = []
n = int(input())
for i in range(n):
    nome, sob, alt, massa = input().split()
    alt = int(alt)
    distAlt = abs(alt-180)
    massa = int(massa)
    if massa <= 75:
        distMass = abs(massa - 75)
    else:
        distMass = abs(massa-75) + 100
    pretendentes.append((nome, sob, massa, distMass, distAlt))

pretendentes = sorted(
    pretendentes, key=lambda pretendentes: pretendentes[0])
pretendentes = sorted(
    pretendentes, key=lambda pretendentes: pretendentes[1])
# pretendentes = sorted(
#     pretendentes, key=lambda pretendentes: pretendentes[2])
pretendentes = sorted(
    pretendentes, key=lambda pretendentes: pretendentes[3])
pretendentes = sorted(
    pretendentes, key=lambda pretendentes: pretendentes[4])
for n in pretendentes:
    print("%s, %s" % (n[1], n[0]))
