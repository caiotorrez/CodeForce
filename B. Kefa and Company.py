
entrada = raw_input().split()
amigos = int(entrada[0])
cash = int(entrada[1])

lista = []
convidados = []
for i in range(amigos):
    dinheiro,fator = raw_input().split()
    lista.append((dinheiro,fator))

maior = False
for j in range(len(lista)):
    somador = 0
    somador += int(lista[j][1])
    only = int(lista[j][0])
    for k in range(j+1,amigos):
        
        if abs(int(lista[j][0]) - int(lista[k][0])) < cash:
            if abs(int(lista[k][0]) - only) < cash:
                somador += int(lista[k][1])
                only = int(lista[k][0])
                
    convidados.append(somador)
    if maior == False:
        maior = True
        maximo = convidados[0]
    if maior == True:
        if convidados[j] > maximo:
            maximo = convidados[j]


print str(maximo)
