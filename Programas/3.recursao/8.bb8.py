# Programa errado!!! N funciona

def verificarChao(cordBb8, cordArt):
    if cordArt == cordBb8:
        return True
    else:
        return False


def verificarSeFoiVisitado(cord, allcords):
    if cord in allcords:
        return True
    else:
        return False


def registrarComoVisitado(cord, allcords):
    allcords.append(cord)


def verificarNorte(cord, cords):
    if cord in cords:
        return True
    else:
        return False


def verificarSul(cord, cords):
    if cord in cords:
        return True
    else:
        return False


def verificarLeste(cord, cords):
    if cord in cords:
        return True
    else:
        return False


def verificarOeste(cord, cords):
    if cord in cords:
        return True
    else:
        return False


def moverNorte(cord, nextcord):
    try:
        cord = nextcord
        return True
    except:
        return False


def moverSul(cord, nextcord):
    try:
        cord = nextcord
        return True
    except:
        return False


def moverLeste(cord, nextcord):
    try:
        cord = nextcord
        return True
    except:
        return False


def moverOeste(cord, nextcord):
    try:
        cord = nextcord
        return True
    except:
        return False


def buscarArtefato():
    if verificarChao() != None:
        return verificarChao()
    elif verificarNorte() == True:
        moverNorte()
        if verificarSeFoiVisitado() == True:
            moverSul()
        else:
            registrarComoVisitado()
    elif verificarLeste() == True:
        moverLeste()
        if verificarSeFoiVisitado() == True:
            moverOeste()
        else:
            registrarComoVisitado()
    elif verificarSul() == True:
        moverSul()
        if verificarSeFoiVisitado() == True:
            moverNorte()
        else:
            registrarComoVisitado()
    elif verificarOeste() == True:
        moverOeste()
        if verificarSeFoiVisitado() == True:
            moverLeste()
        else:
            registrarComoVisitado()
    return buscarArtefato()
