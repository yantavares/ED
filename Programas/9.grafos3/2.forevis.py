def shortest_path(graph, start, goal):
    explored = []
     
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in explored:
            neighbours = graph[node]
             

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    print(len(new_path)-2)
                    return
            explored.append(node)
 
    print("Forevis alonis...")

n = int(input())

graph = {}

for k in range(n):
    inst = list(map(int, input().split()))
    user = inst[0]
    inst.pop(0)
    inst.pop(0)

    graph[user] = []
    for j in inst:
        graph[user].append(j)

you, mussum = map(int, input().split())

shortest_path(graph, you, mussum)


 