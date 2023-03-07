num1, num2, tipo = input().split()
num1 = int(num1)
num2 = int(num2)


mat = [[0 for i in range(num1)] for i in range(num1)]

if tipo == 'D':
    for i in range(num2):
        x, y, p = map(int,input().split())
        mat[x-1][y-1] = p

else:
    for i in range(num2):
        x, y, p = map(int,input().split())
        mat[x-1][y-1] = p
        mat[y-1][x-1] = p

for k in mat:
    for i in k:
        print(' '*(3-len(str(i))), i, end='')
    print()
