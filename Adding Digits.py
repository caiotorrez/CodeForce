entrada = raw_input().split()

b = int(entrada[1])
n = int(entrada[2])

a = entrada[0]

result = a
i = 0
while i < 10:
    result += str(i)
    if int(result) % b == 0:
        a = result
        break
    result = a
    i += 1
n -= 1

result = result + '0'*n

if int(result) % b == 0:
    print result

else:
    print '-1'
