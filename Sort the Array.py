def verifica(final, lista):
    for i in range(final,len(lista)-1):
        if int(lista[i]) > int(lista[i+1]):
            return False
    return True

def array(lista):
    decrescente = False
    
    inicio = 0
    for i in range(len(lista)-1):

        if decrescente == False and int(lista[i]) > int(lista[i+1]):
            decrescente = True
            inicio = i

        if decrescente == True and int(lista[i]) < int(lista[i+1]):
            fim = i

            return inicio,fim
    if decrescente == True:
        return inicio,len(lista)
    else:
        return 0,0

none = raw_input()
lista = raw_input().split()

i,f = array(lista)

if f < len(lista):
    flag = verifica(f,lista)

try:
    if i+f == 0:
        print 'yes'
        print '1 1'
        
    elif i == 0 and  f == len(lista):
        print 'yes'
        print i+1,f

    elif i == 0 and int(lista[f]) and int(lista[f+1]) > int(lista[i]) and flag == True:
        print 'yes'
        print i+1,f+1

    elif f == len(lista) and int(lista[i-1]) < int(lista[f-1]):
        print 'yes'
        print i+1,f
        
        
    elif int(lista[i-1]) < int(lista[f]) and int(lista[f+1]) > int(lista[i]) and flag == True:
        print 'yes'
        print i+1,f+1
        
    else:
        print 'no'
except:
    print 'no'
