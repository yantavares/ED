# Usei a implementaçao de pilha feita na questao 3

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            pass
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            pass
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


peso = 0
count = 0
anilhas = Stack()

while True:
    x = int(input())
    if x == 0:
        break
    else:
        anilhas.push(x)
y = int(input())

if anilhas.size() != 0:

    while True:
        print("Peso retirado:", anilhas.peek())
        temp = anilhas.pop()
        peso += temp
        count += 1
        if y == temp:
            break

    print('Anilhas retiradas:', count)
    print('Peso total movimentado:', peso)
else:
    print('Anilhas retiradas:', 0)
    print('Peso total movimentado:', 0)
