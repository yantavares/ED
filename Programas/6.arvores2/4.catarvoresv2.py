class ArvoreBinaria:
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificaPontuacao(raiz, v1, v2):
    if not raiz:
        return

    if v1 == v2:
        return v1
    
    if raiz.dado == v1:
        return v1
    elif raiz.dado == v2:
        return v2

 
    x = verificaPontuacao(raiz.esq, v1, v2)
    y = verificaPontuacao(raiz.dir, v1, v2)

    if x and y:
        return raiz.dado
 
    if x:
        return x
    if y:
        return y

raiz = ArvoreBinaria(6)

raiz.esq = ArvoreBinaria(11)
raiz.dir = ArvoreBinaria(2)

raiz.esq.esq = ArvoreBinaria(12)
raiz.esq.dir = ArvoreBinaria(8)

raiz.dir.esq = ArvoreBinaria(4)
raiz.dir.dir = ArvoreBinaria(7)


print(verificaPontuacao(raiz, 6, 4))
print(verificaPontuacao(raiz, 11, 4))
print(verificaPontuacao(raiz, 12, 4))
print(verificaPontuacao(raiz, 8, 4))
print(verificaPontuacao(raiz, 2, 4))
print(verificaPontuacao(raiz, 4, 4))
print(verificaPontuacao(raiz, 7, 4))