from itertools import combinations


def caetanao(premios):
    somas = []
    for n in range(1, len(premios)):
        combos = list(combinations(premios, n))
        for i in combos:
            somas.append(sum(i))
    return somas


count = 0
premios = list(map(int, input().split()))
s = int(input())
for n in caetanao(premios):
    if n == s:
        print("E possivel ganhar.")
        count += 1
        break
if count == 0:
    print("Impossivel ganhar.")
