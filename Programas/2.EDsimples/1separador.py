x = input()
x = x.split()

num = []
pal = []

for i in x:
    try:
        int(i)
        num.append(i)
    except:
        pal.append(i)

num = num[::-1]
pal = pal[::-1]


print("Palavras:")
print(*pal, sep="\n")
print("")
print("Numeros:")
print(*num, sep="\n")
