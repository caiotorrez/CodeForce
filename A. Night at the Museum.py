
horario = 97
anti = 97
total = 0

palavra = raw_input()
for j in range(len(palavra)):
    somador = 0
    fixo = ord(palavra[j])
    while True:

        if horario == fixo:
            total += somador
            anti = fixo
            break

        elif anti == fixo:
            total += somador
            horario = fixo

            break

        horario += 1
        anti -= 1
        somador += 1

        if horario > 122:
            horario = 97

        if anti < 97:
            anti = 122
print total
