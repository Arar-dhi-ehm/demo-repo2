
def pattern(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, i+1):
            print('* ', end='')
        print('\r')
    for i in range(n, 0, -1):
        for j in range(0, i+1):
            print('* ', end='')
        print('\r')

pattern(5)