while True:
    try:
        s = input()
        n, l, u, d = 0, 0, 0, 0
        for c in s:
            if c.islower():
                l += 1
            if c.isupper():
                u += 1
            if c.isdigit():
                d += 1
            if l >= 1 and u >= 1 and d >= 1:
                n += 1
                l, u, d = 0, 0, 0
        print(n)
    except:
        break
