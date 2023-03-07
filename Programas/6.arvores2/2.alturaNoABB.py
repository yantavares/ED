class ArvoreBinaria:
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def nivel(raiz, n, altura=0):
    if not raiz:
        return -1
    
    if raiz.dado == n:
        return altura
    
    x = nivel(raiz.esq, n, altura+1)

    if x == -1:
        return nivel(raiz.dir, n, altura+1)
        

    return nivel(raiz.esq, n, altura+1)
