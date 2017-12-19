
def shovel(valor, moeda):
    i = 1
    while True:   
        if valor*i % 10 == moeda or valor*i % 10 == 0:
            return i

        i += 1

x,y = map(int, raw_input().split())
print shovel(x,y)
