n = int(input())
x = 0
for i in range(n):
    palavra = list(input())
    lista = []
    for i in range(3):
        b = list(input())
        for k in b:
            if k in palavra:
                palavra.remove(k)
            else:
                lista.append(k)
    if lista != []:
        print('You died!')
    elif palavra != []:
        palavra = sorted(set(palavra))
        palavra = ''.join(palavra)
        print('Bora ralar: %s' % palavra)
    else:
        print("It's in the box!")
