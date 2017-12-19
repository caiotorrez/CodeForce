import sys



n, m = map(int, raw_input().split())

way = map(int, raw_input().split())

memo = [0]
j = 0
for i in xrange(m):

    if memo[j] > way[i]:
        memo.append(way[i])
        j += 1
    else:
        memo[j] = way[i]

if len(memo) > 1:
        
    result = n * (len(memo) -1) + memo[-1] - 1
else:
    result = memo[0] - 1

print result
