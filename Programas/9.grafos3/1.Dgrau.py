grafo = {}
n = int(input())

if n == 0:
    print(0)

else:

    for l in range(n):
        inst = input().split()
        if inst[0] == 'IV' and inst[1] not in grafo:
            grafo[inst[1]] = []
        
        elif inst[0] == 'IA':
            if inst[1] in grafo and inst[2] in grafo:
                if inst[2] not in grafo[inst[1]]:
                    grafo[inst[1]].append(inst[2])
                    grafo[inst[2]].append(inst[1])
        
        elif inst[0] == 'RV':
            if inst[1] in grafo:
                grafo.pop(inst[1])
                for i in grafo:
                    if inst[1] in grafo[i]:
                        grafo[i].remove(inst[1])
        
        elif inst[0] == 'RA':
            if inst[1] in grafo and inst[2] in grafo:
                if inst[2] in grafo[inst[1]]:
                    grafo[inst[1]].remove(inst[2])
                    grafo[inst[2]].remove(inst[1])
    
    tam = []
    for k in grafo:
        tam.append(len(grafo[k]))

    print(min(tam))
