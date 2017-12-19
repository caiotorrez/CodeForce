import sys

v1, v2 = map(int, raw_input().split())
t, d = map(int, raw_input().split())
 
distancia = v1
for i in xrange(1, t-1):
    distancia += min(v1 + i*d, (v2 + (t-1)*d) - i*d)
 
distancia += v2
sys.stdout.write(str(distancia) + '\n')
