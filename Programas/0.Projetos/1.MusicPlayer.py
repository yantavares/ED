instrucao = ''
pos = 0
tocando = False
musicas = []
count = -1
estados = [[[], 0, False]]
estadoinicial = estados.copy()
passouEnded = False
podeUndo = False

while instrucao != 'fight':
    passouPorAqui = False
    podeUndo = False
    instrucao = input()
    if 'add' in instrucao:
        podeUndo = True
        musicas.append(instrucao[4:])
    elif 'list' == instrucao:

        if musicas == []:
            print('[Vazia]')
        else:
            print(*musicas, sep=',')

    elif 'play' == instrucao:
        if tocando == True:
            pass
        else:
            podeUndo = True
            tocando = True
    elif 'stop' == instrucao:
        tocando = False
    elif 'del' in instrucao and instrucao[4:] in musicas:
        podeUndo = True
        if tocando == True:
            if musicas[pos] != instrucao[4:]:
                k = musicas.index(instrucao[4:])
                if k >= pos:
                    musicas.remove(instrucao[4:])
                else:
                    musicas.remove(instrucao[4:])
                    pos -= 1
            else:
                podeUndo = False
        else:
            k = musicas.index(instrucao[4:])
            if k >= pos:
                musicas.remove(instrucao[4:])
            else:
                musicas.remove(instrucao[4:])
                pos -= 1
    elif 'ended' == instrucao:
        if tocando == True:
            passouEnded = True
            if pos < len(musicas) - 1:
                pos += 1
            else:
                pos = 0
    elif 'next' in instrucao:

        if tocando == True and instrucao[5:] == musicas[pos] or instrucao[5:] not in musicas:
            pass
        elif tocando == False and pos == 0:
            podeUndo = True
            musicas.remove(instrucao[5:])
            musicas.insert(0, instrucao[5:])
        else:
            podeUndo = True
            x = musicas.index(instrucao[5:])
            if x < pos:
                pos -= 1
            musicas.pop(x)
            musicas.insert(pos+1, instrucao[5:])
    elif 'current' == instrucao:
        if musicas == []:
            print("Toque! Toque, Dijê!")
        else:
            print(musicas[pos])
    elif 'undo' in instrucao:
        passouPorAqui = True
        if '*' not in instrucao:
            if len(estados) <= 1:
                pass
            else:
                estados.pop()
                musicas = estados[-1][0].copy()
                pos = estados[-1][1]
                tocando = estados[-1][2]
                '''
                count -= 1
                musicas = estados[count][0].copy()
                pos = estados[count][1]
                tocando = estados[count][2]
                estados.pop()
                '''

        else:

            if estados == []:
                pass
            else:
                estados.clear()
                estados = estadoinicial.copy()

                musicas = estados[0][0].copy()
                pos = estados[0][1]
                tocando = estados[0][2]

    if passouEnded == True:

        if estados == []:
            passouEnded = False
            pass
        else:
            estados.append([musicas.copy(), pos, tocando])
            estadoinicial = []
            estadoinicial.append(estados[-1].copy())
            estados = estadoinicial.copy()

            musicas = estados[0][0].copy()
            pos = estados[0][1]
            tocando = estados[0][2]
            count = 0
            passouEnded = False
    else:
        if passouPorAqui == False and podeUndo == True:
            estados.append([musicas.copy(), pos, tocando])
        elif passouPorAqui == False and podeUndo == False:
            if estados == []:
                pass
            else:
                estados.pop()
                estados.append([musicas.copy(), pos, tocando])
        else:
            count -= 1

    count += 1
print('Jedi Wagner, assuma o comando!')
