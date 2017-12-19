lenght, values = map(int, raw_input().split())
array = map(int, raw_input().split())
add = 0
for i in xrange(values):
    op = map(int, raw_input().split())

    if op[0] == 1:
        array[op[1] - 1] = op[2] - add

    elif op[0] == 2:
        add += op[1]
        
    else:
        print array[op[1] - 1] + add
