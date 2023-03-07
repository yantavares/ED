def analisa(x, y):
    if x < y:
        x, y = y, x
    print(x)
    print(y)
    if x == y:
        print("iguais")
    else:
        print("diferentes")
