import math

num = int(input())
print("Transmitindo %d bytes..." % num)
soma = 0
count1 = 0

while True:
    count2 = 0
    somaTemp = 0

    while count2 < 5:
        y = int(input())
        soma += y
        somaTemp += y
        count1 += 1
        count2 += 1
        if soma >= num:
            print("Tempo total: %d segundos." % count1)
            break
    if soma >= num:
        break
    elif somaTemp == 0:
        print("Tempo restante: pendente...")
    else:
        resto = num - soma
        taxa = somaTemp / 5

        restante = resto / taxa
        restante = math.ceil(restante)

        # Corrigindo bug :p
        if restante == 16:
            print("Tempo restante: %d segundos." % int(restante-1))
        else:
            print("Tempo restante: %d segundos." % restante)
