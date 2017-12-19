import sys

spaces, lenght = map(int, raw_input().split())


dic = {}

for i in xrange(lenght):

    w1, w2 = raw_input().split()
    if len(w1) > len(w2):
        menor = w2
        maior = w1

    else:
        menor = w1
        maior = w2
        
    dic[maior] = menor
    dic[menor] = menor


frase = raw_input().split()

for i in xrange(len(frase)):

    sys.stdout.write(dic[frase[i]])
    if i < len(frase) -1:
        sys.stdout.write(' ')
sys.stdout.write('\n')
