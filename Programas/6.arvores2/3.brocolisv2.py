def brocolis():
    baseEsq = [0, 1]
    baseDir = [1, 0]
    inicio = [1, 1]
    estados = []
    s = input()
    ultimo = ''
    if s == '':
        pass
    elif s[0] == 'E':
        base = baseEsq
        ultimo = 'E'
    else:
        base = baseDir
        ultimo = 'D'
    for i in s:
        if (i == 'E' and ultimo == 'E') or (i=='D' and ultimo == 'D'):
            estados.append(inicio.copy())
            inicio[0] += base[0]
            inicio[1] += base[1]
            if i == 'E':
                ultimo = 'E'
            else:
                ultimo = 'D'
            
        else:
            base = estados[-1].copy()
            estados.append(inicio.copy())
            
            inicio[0] += base[0]
            inicio[1] += base[1]
            if i == 'E':
                ultimo = 'E'
            else:
                ultimo = 'D'

                
    print('%d / %d' %(inicio[0], inicio[1]))

n = int(input())

for k in range(n):
    brocolis()