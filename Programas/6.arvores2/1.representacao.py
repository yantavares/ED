def temFilho(raiz):
    try:
        raiz.filho
        return True
    except:
        return False

def printaRaiz(raiz, sep):
    try:
        print(raiz.dado)
        sep0 = sep
        return sep0
    except:
        pass

def main(raiz, sep):
    global sep0
    printaRaiz(raiz, sep)
    if not raiz:
        return
    if type(raiz) == list:
        for n in raiz:
            print(sep, n.dado, sep="")
            if temFilho:
                main(n.filhos, sep + sep0)
    else:
        main(raiz.filhos, sep)

def mostra(raiz, sep):
    global sep0
    sep0 = sep
    main(raiz, sep)

