num = int(input())

arist = []

for k in range(num):
    caminho = input().split()
    arist.append((caminho[0] ,caminho[1:]))

pesquisa = input().split()

for w in arist:
    for i in pesquisa:
        if i in w[1]:
            print(w[0])
            break
