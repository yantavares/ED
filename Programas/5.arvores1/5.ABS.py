class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def simetria(raiz1, raiz2):
    if not raiz1 and not raiz2:
        return True
    if raiz1 and raiz2 and raiz1.dado == raiz2.dado:
        return (simetria(raiz1.esq, raiz2.dir) and simetria(raiz1.dir, raiz2.esq))
    return False

def verificaSimetria(raiz):
    return simetria(raiz, raiz)
    

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(3, ArvoreBinaria(0, ArvoreBinaria(4, None, None), ArvoreBinaria(7, None, None)), None)
print(verificaSimetria(raiz))