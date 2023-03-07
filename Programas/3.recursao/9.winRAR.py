def decompress(n):
    letras = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0:
        return ''
    else:
        temp = n % 2**5
        return letras[temp] + decompress(n//2**5)
