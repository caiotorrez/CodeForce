def maximo(lista):

    custo = []

    if int(lista[0]) < 0:
        if int(lista[-1]) < 0:
            custo.append(abs((abs(int(lista[-1]))) - (abs(int(lista[0])))))
        else:
            custo.append((abs(int(lista[0]))) + int(lista[-1]))
    else:
        custo.append(int(lista[-1]) - int(lista[0]))
        
    for i in range(1,len(lista)-1):
        
        if int(lista[0]) < 0:
            if int(lista[i]) > 0:
                if abs(int(lista[0])) + int(lista[i]) > int(lista[-1]) - int(lista[i]):
                    maior = abs(int(lista[0])) + int(lista[i])

                else:
                    maior = int(lista[-1]) - int(lista[i])

            else:
                if abs(int(lista[0]) - int(lista[i])) > int(lista[-1]) - int(lista[i]):
                    maior = abs(int(lista[0]) - int(lista[i]))

                else:
                    maior = int(lista[-1]) - int(lista[i])
                    
        else:
            if int(lista[-1]) - int(lista[i]) > int(lista[i]) - int(lista[0]):
                maior = int(lista[-1]) - int(lista[i])

            else:
                maior = abs(int(lista[i]) - int(lista[0]))

        custo.append(maior)

    if int(lista[-1]) < 0:
        custo.append(abs((abs(int(lista[-1]))) - abs(int(lista[0]))))
    else:
        if int(lista[0]) < 0:
            custo.append(int(lista[-1]) + abs(int(lista[0])))
        else:
            custo.append(int(lista[-1]) - int(lista[0]))
            
    return custo

def minimo(lista):
        
    custo = []

    if int(lista[0]) >= 0:
        custo.append(int(lista[1]) - int(lista[0]))
    elif int(lista[1]) < 0:
        custo.append(abs(int(lista[0])) - abs(int(lista[1])))
    else:
        custo.append((abs(int(lista[0]))) + int(lista[1]))

    for i in range(1,len(lista)-1):

        if int(lista[i]) < 0:
            if int(lista[i+1]) < 0:
                if abs(int(lista[i])) - abs(int(lista[i+1])) < abs(int(lista[i-1])) - abs(int(lista[i])):
                    menor = abs(int(lista[i])) - abs(int(lista[i+1]))
                    
                else:
                    menor = abs(int(lista[i-1])) - abs(int(lista[i]))

            else:
                if abs(int(lista[i-1])) - abs(int(lista[i])) < abs(int(lista[i])) + int(lista[i+1]):
                    menor = abs(int(lista[i-1])) - abs(int(lista[i]))

                else:
                    menor = abs(int(lista[i])) + int(lista[i+1])

        else:
            if int(lista[i-1]) < 0:
                if abs(int(lista[i-1])) + int(lista[i]) < int(lista[i+1]) - int(lista[i]):
                    menor = abs(int(lista[i-1])) + int(lista[i])

                else:
                    menor = int(lista[i+1]) - int(lista[i])
                    
            else:
                if int(lista[i]) - int(lista[i-1]) < int(lista[i+1]) - int(lista[i]):
                    menor = int(lista[i]) - int(lista[i-1])

                else:
                    menor = int(lista[i+1]) - int(lista[i])

        custo.append(menor)

                
    if int(lista[-1]) >= 0:
        custo.append(int(lista[-1]) - int(lista[-2]))
    elif int(lista[-2]) < 0:
        custo.append(abs(int(lista[-2])) - abs(int(lista[-1])))
    else:
        custo.append((abs(int(lista[-1]))) - int(lista[-2]))

    return custo


cidades = int(raw_input())
lista = raw_input().split()


custo_max = maximo(lista)
custo_min = minimo(lista)
for i in range(len(lista)):
    
    print '%s %s' %(custo_min[i], custo_max[i])
