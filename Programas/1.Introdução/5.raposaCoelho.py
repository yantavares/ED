import math

n = int(input())
coelhox, coelhoy = map(float, input().split(" "))
raposax, raposay = map(float, input().split(" "))
buracos = []
for k in range(n):
    buracox, buracoy = map(float, input().split(" "))
    buraco = [buracox, buracoy]
    buracos.append(buraco)

count = 0

for i in buracos:
    raposaBuraco = math.sqrt((i[0] - raposax)**2 + (i[1] - raposay)**2)
    coelhoBuraco = math.sqrt((coelhox - i[0])**2 + (coelhoy - i[1])**2)

    if coelhoBuraco * 2 < raposaBuraco:
        print("O coelho pode escapar pelo buraco (%0.3f, %0.3f)." %
              (i[0], i[1]))
        break
    count += 1

if count == n:
    print("O coelho nao pode escapar.")
