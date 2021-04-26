def numsteps(c):
    z = 0
    i = 0
    while z < 2:
        z = z*z + c
        i += 1
    print(i)
