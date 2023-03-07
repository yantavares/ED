n = int(input())

def brocolis(n):
    lst = ['0 / 1', '1 / 1', '1 / 0']
    temp = lst.copy()
    j = 1
    for k in range(n):
        for i in range(len(lst)-1):

            ind1 = lst[i].index('/')
            ind2 = lst[i+1].index('/')
            num1 = int(lst[i][:ind1-1]) + int(lst[i+1][:ind2-1])
            num2 = int(lst[i][ind1+2:]) + int(lst[i+1][ind2+2:])

       
            temp.insert(j, str(num1) + ' / ' + str(num2))
            j += 2

        lst = temp.copy()
        j = 1

            

    return lst

arvore = []

for k in range(n):
    inst = input()
    tam = len(inst)
    arvore = brocolis(tam)
    index = len(arvore) // 2
    ajuste = 2**(tam-1)
    for j in inst:
        if j == 'D':
            index += ajuste
        else:
            index -= ajuste
        ajuste //= 2
    print(arvore[index])
