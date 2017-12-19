
def relogio(formato, horas, minutos):
    
    h = ''
    m = ''
    if formato == 12:
        if int(minutos) >= 60:
            m = '0' + minutos[1]

        elif int(minutos) < 60:
            m = minutos

        if int(horas) > 12:
            if int(horas[0]) > 1 and (int(horas[1])) < 3:
                h = '1' + horas[1]
            else:
                h = '0' + horas[1]

        elif int(horas) <= 12:
            h = horas

        if h == '00' or horas == '00':
            h = '01'
               
        return h,m    

    elif formato == 24:
        if int(minutos) >= 60:
            m = '0' + minutos[1]

        elif int(minutos) < 60:
            m = minutos
            
        if int(horas) > 23:
             h = '0' + horas[1]
             return h,m

        else:
            return horas,m


formato = int(raw_input())
tempo = raw_input().split(':')
horas = tempo[0]
minutos = tempo[1]

print '%s:%s' %(relogio(formato, horas, minutos))
