dic = {}
lst = []
valor = 0
while True:
    x = input()
    if x == 'fim':
        break
    else:
        x, y = x.split()
        if x == "-":
            dic.pop(y)
        else:
            y = float(y)
            dic[x] = y

for i in dic:
    lst.append([i, dic[i]])

lst = lst[::-1]
for i in lst:
    valor += i[1]
    print("%s: R$ %.2f" % (i[0], i[1]))
print("----------------------")
print("%d item(ns): R$ %.2f" % (len(lst), valor))
