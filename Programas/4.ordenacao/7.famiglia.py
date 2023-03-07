n = int(input())

casas = list(map(int, input().split()))
casas = sorted(casas)
soma = 0
soma2 = 0
if n == 1:
    print(casas[0])
elif n == 2:
    print(abs(casas[1] - casas[0]))
elif n % 2 == 1:
    pos = n//2
    for i in range(pos):
        soma += abs(casas[pos] - casas[i])
    for j in range(pos+1, n):
        soma += abs(casas[pos] - casas[j])
    print(soma)
elif n % 2 == 0:
    pos1 = n // 2
    pos2 = pos1 - 1
    for i in range(pos1):
        soma += abs(casas[pos1] - casas[i])
    for j in range(pos1+1, n):
        soma += abs(casas[pos1] - casas[j])
    for k in range(pos2):
        soma2 += abs(casas[pos2] - casas[k])
    for l in range(pos2+1, n):
        soma2 += abs(casas[pos2] - casas[l])

    if soma2 <= soma:
        print(soma2)
    else:
        print(soma)
