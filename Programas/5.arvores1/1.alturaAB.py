class ArvoreBinaria:
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def altura(raiz):
    if not raiz:
        return 0
    if raiz.esq and raiz.dir:
        return 1 + max(altura(raiz.esq), altura(raiz.dir))
    elif raiz.esq:
        return 1 + altura(raiz.esq)
    elif raiz.dir:
        return 1 + altura(raiz.dir)
    else:
        return 0

'''
Mostrar Árvore

def mostra(raiz):
    if not raiz:
        return

    print(raiz.dado)
    mostra(raiz.dir)
    mostra(raiz.esq)
'''
