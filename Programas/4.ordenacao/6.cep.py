ceps = []
count = 0
n = int(input())

for i in range(n):
    cep = input()
    ceps.append(cep)

ceps = sorted(ceps)

for i in range(1, len(ceps)):
    for j in range(len(ceps[0])):

        if ceps[i][j] == ceps[i-1][j]:
            count += 1

end = count * (7 / 100)

print("R$ %.2f" % end)
