dinheiro = int(raw_input())
plastico = int(raw_input())
vidro = int(raw_input())
retornavel = int(raw_input())

qt_vidro = 0
qt_plastico = 0

if dinheiro >= plastico:
    qt_plastico = dinheiro / plastico

if dinheiro >= vidro:
    qt_vidro = ((dinheiro - retornavel) / (vidro - retornavel))
    dinheiro = dinheiro - ((vidro - retornavel) * qt_vidro)

    if dinheiro >= plastico:
        qt_vidro += dinheiro / plastico
        
if qt_plastico >= qt_vidro:
    print qt_plastico
        
elif qt_vidro > 0:
    print qt_vidro
            
else:
    print '0'
