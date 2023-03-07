n = int(input())

hab = input().split(" ")
hab = list(map(int, hab))

maiores = []

for i in range(11):
    temp = hab[:]
    while len(temp) > 1:
        k = len(temp) - 1
        if temp[k] > temp[k-1]:
            temp.pop(k-1)
        else:
            temp.pop(k)
    hab.remove(temp[0])
    maiores.append(temp[0])

if len(hab) > 11:
    for i in range(len(hab) - 11):
        temp = hab[:]
        while len(temp) > 1:
            k = len(temp) - 1
            if temp[k] < temp[k-1]:
                temp.pop(k-1)
            else:
                temp.pop(k)
        hab.remove(temp[0])

somaMaiores = 0
somaMenores = 0

for i in maiores:
    somaMaiores += i

for i in hab:
    somaMenores += i

print(somaMaiores - somaMenores)
