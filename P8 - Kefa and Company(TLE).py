def search(array):
    total = [0]*friends*2
    for i in xrange(friends/10+1):
        for j in xrange(i,friends):
            if array[j][0] - array[i][0] < diference:
                total[i] += array[j][1]
                
            if array[-i-1][0] - array[-j-1][0] < diference:
                total[-i-1] += array[-j-1][1]

            else:
                break

    return max(total)

array = []
friends, diference = map(int, raw_input().split())
for i in xrange(friends):
    array.append((map(int, raw_input().split())))

array.sort()
print search(array)
