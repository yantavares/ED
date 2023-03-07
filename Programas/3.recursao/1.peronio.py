def peronio(a, b):
    if len(a) == 0 or len(b) == 0:
        return 1
    elif a[0] == b[0]:
        return 1 + peronio(a[1:], b[1:])
    else:
        return 1
