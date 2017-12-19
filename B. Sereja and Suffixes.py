
n, m = map(int, raw_input().split())

array = map(int, raw_input().split())

suport = [0]*100001
total = [0]
for i in xrange(len(array)):

    if suport[array[-i-1]] == 0:
        suport[array[-i-1]] = 1
        total.append(total[i] + 1)

    else:
        total.append(total[i])

for i in xrange(m):

    print total[-int(raw_input())]
