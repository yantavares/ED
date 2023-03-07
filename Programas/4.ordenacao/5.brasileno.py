import math
times = []
pontoTotal = 0
for i in range(20):
    pontos = 0
    golsS = 0
    golsM = 0
    vit = 0
    n = input().split()
    nome = n[0]

    for i in range(1, len(n)):
        golsM += int(n[i][0])
        golsS += int(n[i][2])
        if int(n[i][0]) > int(n[i][2]):
            vit += 1
            pontoTotal += 3
            pontos += 3
        elif int(n[i][0]) == int(n[i][2]):
            pontos += 1
            pontoTotal += 1
    saldo = golsM - golsS

    times.append((pontos, vit, saldo, golsM, golsS, nome))


mediaPontos = pontoTotal/20
times = sorted(times, key=lambda times: times[5])
times = sorted(times, key=lambda times: times[4])
times = sorted(times, key=lambda times: times[3], reverse=True)
times = sorted(times, key=lambda times: times[2], reverse=True)
times = sorted(times, key=lambda times: times[1], reverse=True)
times = sorted(times, key=lambda times: times[0], reverse=True)

print("Media de pontos: %.2f" % mediaPontos)
print("Liberadores: %s, %s, %s, %s" %
      (times[0][5], times[1][5], times[2][5], times[3][5]))
print("Rebaixados: %s, %s, %s, %s" %
      (times[19][5], times[18][5], times[17][5], times[16][5]))
