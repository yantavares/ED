def constituiArvoreBinariaDeBusca(raiz):
 
    if not raiz:
        return True

    if raiz.esq and raiz.dado <= raiz.esq.dado:
        return False
 
    if raiz.dir and raiz.dado >= raiz.dir.dado :
        return False
 

    return constituiArvoreBinariaDeBusca(raiz.esq) and \
        constituiArvoreBinariaDeBusca(raiz.dir)