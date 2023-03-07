num = int(input())

andou = {'N': 0, 'L': 0}
voltar = {'N': 0, 'S':0, 'L': 0, 'O':0}

for k in range(num):
    dire, dist = input().split()
    dist = int(dist)

    if dire == 'N':
        andou['N'] += dist
    elif dire == 'S':
        andou['N'] -= dist
    elif dire == 'L':
        andou['L'] += dist
    else:
        andou['L'] -= dist

if andou['N'] >= 0:
    voltar['S'] = andou['N']

if andou['N'] < 0:
    voltar['N'] = -andou['N']

if andou['L'] >= 0:
    voltar['O'] = andou['L']

if andou['L'] < 0:
    voltar['L'] = -andou['L']


for w in voltar:
    print(voltar[w], end= ' ')
print()