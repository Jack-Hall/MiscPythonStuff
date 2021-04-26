def check(num):
    lit = [0]*10
    for i in range(len(pins)):
        if((num -(i+1)*10) > 10):
            lit[i] = 100
        elif((num -(i+1)*10) > 1):
            lit[i] = num - (i+1)*100
    return lit
