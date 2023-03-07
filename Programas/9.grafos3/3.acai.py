end = []
def prims(size, graph):

    inf = 9999999
    selected_node = mat = [0 for i in range(size)]

    no_edge = 0
    selected_node[0] = True
    while (no_edge < size - 1):
        
        minimum = inf
        a = 0
        b = 0
        for m in range(size):
            if selected_node[m]:
                for n in range(size):
                    if ((not selected_node[n]) and graph[m][n]):  
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
        end.append(graph[a][b])
        selected_node[b] = True
        no_edge += 1

n = int(input())

if n == 1:
    print('R$ 0.00')

else:
    houses = []
    dist = []
    for count in range(n):
        inst = list(map(int, input().split()))

        house = inst[0]
        size = inst[1]

        houses.append(house)
        inst.pop(0)
        inst.pop(0)

        for k in range(1 ,size*2, 2):
            dist.append((house, inst[k], inst[k-1]))


    mat = [[0 for i in range(n)] for i in range(n)]

    for i in dist:
        mat[i[0]-1][i[1]-1] = i[2]
        mat[i[1]-1][i[0]-1] = i[2]

    prims(n, mat)
    price = 0
    for i in end:
        price += i
    
    price*=3.14

    print('R$ %.2f' % price)