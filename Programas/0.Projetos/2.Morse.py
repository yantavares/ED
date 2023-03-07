def main():
    deuBom = True
    mensagem = ''
    chars = {}
    morse = {}
    n = int(input())

    for k in range(n):
        x, y = input().split()

        chars[x] = y
        morse[y] = x
    
    end = int(input())

    #Decodificando
    if end == 0:
        code = input().split()
        for i in code:
            if '/' in i:
                mensagem += ' '
                i = i[1:]
            if i in morse:
                mensagem += morse[i]
            else:
                mensagem = 'Impossível decodificar a mensagem!'
                deuBom = False
                break

    #Codificando
    else:
        code = input()
        for i in code:
            if i == ' ':
                if mensagem[-1] != '/':
                    mensagem += '/'
            elif i in chars:
                mensagem += chars[i]
                mensagem += ' '
            else:
                mensagem = 'Impossível codificar a mensagem!'
                deuBom = False
                break
    

    newChars = list(chars.items())
    for k in newChars:
        if len(k[1]) > 1 and k[1][:-1] not in morse:
            newChars.append(('*', k[1][:-1]))
            morse[k[1][:-1]] = '*'

    newChars = sorted(newChars, key= lambda x: x[1], reverse= True)  
    newChars = sorted(newChars, key=lambda x: len(x[1]))

    print(mensagem)

    if deuBom:
        print('*', end= ' ')
        for n in newChars:
            print(n[0], end=' ')
        print()

main()