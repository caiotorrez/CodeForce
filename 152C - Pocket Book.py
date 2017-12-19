

coluna, linha = map(int, raw_input().split())
lista = []

for j in xrange(coluna):
    lista.append(raw_input().split())

total = 1
for l in xrange(linha):
    temp = []
    for i in xrange(coluna):
        temp.append(lista[i][0][l])

    total *= len(set(temp))

print total % 1000000007
        
            
