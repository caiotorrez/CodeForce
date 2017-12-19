
n = int(raw_input())
total = 0

while True:
    
    if n == 1000000000:
        print '8888888899'
        break
        
    elif n <= 999999999 and n > 99999999:
        total += (n - 99999999) * 9
        n -= (n - 99999999)

    elif n <= 99999999 and n > 9999999:
        total += (n - 9999999) * 8
        n -= (n - 9999999)

    elif n <= 9999999 and n > 999999:
        total += (n - 999999) * 7
        n -= (n - 999999)

    elif n <= 999999 and n > 99999:
        total += (n - 99999) * 6
        n -= (n - 99999)

    elif n <= 99999 and n > 9999:
        total += (n - 9999) * 5
        n -= (n - 9999)

    elif n <= 9999 and n > 999:
        total += (n - 999) * 4
        n -= (n - 999)

    elif n <= 999 and n > 99:
        total += (n - 99) * 3
        n -= (n - 99)

    elif n <= 99 and n > 9:
        total += ((n - 9) * 2)
        n -= (n-9)

    elif n <= 9:
        total += n
        print total
        break
