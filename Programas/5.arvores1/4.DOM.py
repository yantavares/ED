raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}}
raiz2 = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}}
raiz3 = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'header', 'P': 'Lorem', 'p': 'ipsum', 'div': {'P': 'wat?'}}}}
raiz4 = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'header', 'P': 'Lorem', 'Y': 'ipsum'}}}

end = []
def main(raiz, pal):
    global end
    if '*' in pal:
        if pal == '*':
            pal = ''
        elif '*' == pal[-1]:
            x = pal.index('*')
            pal = pal[:x]
        elif '*' == pal[0]:
            x = pal.index('*')
            pal = pal[x+1:]
        else:
            pal = pal.replace('*', '')
    for n in raiz:
        if pal.lower() in n.lower():
            end.append(n)
        if type(raiz[n]) == dict:
            main(raiz[n], pal)

def getElementById(raiz, pal):
    main(raiz,pal)
    temp = end.copy()
    end.clear()
    return temp

print(sorted(getElementById(raiz, 'H1')))
print(sorted(getElementById(raiz2, 'H*')))
print(sorted(getElementById(raiz3, 'div')))
print(sorted(getElementById(raiz4, '*Y')))