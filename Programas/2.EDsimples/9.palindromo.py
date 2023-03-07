palavras = input().split()
new = []
pal = []
end = []

for n in palavras:

    for i in range(len(n)-2):

        for j in range(i+3,len(n)+1):
            temp = n[i:j]
            if temp == temp[::-1]:
                pal.append(temp)
    
    pal = sorted(pal, key=len)
    

    k = len(pal)-1
    i = k-1
    
    while i >= 0:
        if pal[i] in pal[k]:
            pal.pop(i)
            i -= 1
            k -=1
        else:
            i -=1
    if len(pal) >= 2:
        end.append(n)
    pal = []

for i in end:
    print(i)