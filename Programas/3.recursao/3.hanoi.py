def hanoi(n, origem, destino, temp):
    if n == 1:
        print("Mover de %s para %s." % (origem, destino))
        return 0
    hanoi(n-1, origem, temp, destino)
    print("Mover de %s para %s." % (origem, destino))
    hanoi(n-1, temp, destino, origem)


n, origem, destino, temp = input().split(" ")
n = int(n)
hanoi(n, origem, destino, temp)
