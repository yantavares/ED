def main(raiz):

    if not raiz:
        return

    print(raiz.dado, end=" ")

    if not raiz.esq and not raiz.dir:
        print("() ()", end="")
        return

    print('(', end="")
    main(raiz.esq)
    print(')', end=" ")

    print('(', end="")
    main(raiz.dir)
    print(')', end="")


def mostra(raiz):
    print("(", end="")
    main(raiz)
    print(")", end="")
