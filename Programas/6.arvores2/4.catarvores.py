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


def saoIrmaos(raiz, v1, v2):

    if not raiz:
        return False
 
    end = False
     
    if raiz.esq and raiz.dir:
         
        if raiz.esq.dado == v1 and raiz.dir.dado == v2:
            return True
        elif raiz.esq.dado == v2 and raiz.dir.dado == v1:
            return True
 
    if not raiz.esq:
        end = end or saoIrmaos(raiz.esq, v1, v2)

    if raiz.dir:
        end = end or saoIrmaos(raiz.dir, v1, v2)
         
    return end

def pai(raiz, v1, papai=None):
    if not raiz:
        return

    if raiz.dado == v1:
        return papai
    else:
        pai(raiz.esq, v1, raiz.dado)
        pai(raiz.dir, v1, raiz.dado)


def verificaPontuacao(raiz, v1, v2):
    h1 = nivel(raiz, v1)
    h2 = nivel(raiz, v2)
    
    if h1 <= h2:
        pai(raiz, v1)
    
    else:
        pai(raiz, v2)


# raiz = ArvoreBinaria(1)
# raiz.esq = ArvoreBinaria(4)
# raiz.dir = ArvoreBinaria(6)

# raiz.esq.esq = ArvoreBinaria(5)
# raiz.esq.dir = ArvoreBinaria(0)

# raiz.dir.esq = ArvoreBinaria(3)
# raiz.dir.dir = ArvoreBinaria(2)

# print(verificaPontuacao(raiz, 3, 2))