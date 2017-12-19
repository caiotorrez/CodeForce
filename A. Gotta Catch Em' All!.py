def contador(string):  
    clone = [0]*9
    flagu = True
    flaga = True
    for i in xrange(len(string)):
        if string[i] == 'B':
            clone[0] += 1
        elif string[i] == 'u':
            if flagu:
                clone[1] += 1
                flagu = False
            else:
                clone[7] += 1
                flagu = True
        elif string[i] == 'l':
            clone[2] += 1
        elif string[i] == 'b':
            clone[3] += 1
        elif string[i] == 'a':
            if flaga:
                clone[4] += 1
                flaga = False
            else:
                clone[6] += 1
                flaga = True
        elif string[i] == 's':
            clone[5] += 1
        elif string[i] == 'r':
            clone[8] += 1
    return clone

def resposta(clone):
    
    menor = min(clone)
    ok = 0
    for k in xrange(9):
        if clone[k] >= menor:
            ok += 1     
    if ok == 9:
        return menor
    else:
        return 0

print resposta(contador(raw_input()))
