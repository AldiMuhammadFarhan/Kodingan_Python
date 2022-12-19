n = 10
i = 1
while i <= n:
    k = 1
    while k <= i:
        print(k)
        k = k + 1
    if (i % 2 == 0):
        k = k - 2
        while k >= 1:
            print(k)
            k = k - 1
    i = i-1
