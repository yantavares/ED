class ArvoreBinaria:
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def inserir(raiz, no):
    if not raiz:
        raiz = no

    elif raiz.dado < no.dado:
        if not raiz.dir:
            raiz.dir = no
        else:
            inserir(raiz.dir, no)
    else:
        if not raiz.esq:
            raiz.esq = no
        else:
            inserir(raiz.esq, no)


ignorar = int(input())

nums = list(map(int, input().split()))

raiz = ArvoreBinaria(nums[0])

for n in nums[1::]:
    inserir(raiz, ArvoreBinaria(n))


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


print(altura(raiz))
