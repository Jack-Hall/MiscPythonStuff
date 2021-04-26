import time
def addsub(x, y, z):
    seq1 = None
    seq2 = None
    if z == 0:
        return 0
    if not(z%(x+y) == 0 and (z-x)%(x-y) == 0):
        return -1
    elif(z%(x-y) == 0):
        seq1 = (z//(x-y))*2
    if (z-x)%(x-y) == 0:
        if z == x:
            return 1
        else:
            seq2 = (z-x)//(x-y)*2 + 1
    
    if seq1 < 0:
            seq1 = None
    if seq2 < 0:
            seq2 = None
    if seq1 == None and seq2 == None:
        return -1
        
    elif seq2 == None:
        return seq1
    elif seq1 == None:
        return seq2
    else:
        return min(seq1, seq2)
    
def remMax(items):
    maxof = items[0]
    c = 1
    index = 0
    for i in range(1, len(items)):
        if items[i] > maxof:
            maxof = items[i]
            index = i
            c = 1
        elif items[i] == maxof:
            c = c+1
            if c == 3:
                index = i
    del items[index]
    return items
def numDigs(string):
    length = len(string)
    for c in string:
        if c != 9:
            return length 
    return length + 1
def bigStr():
    string = '9'
    for i in range(6):
        string = string*10
    return string

def rand7():
    tick = time.time()
    
    return int((time.time() * pow(10,10)) % 7)

def keeptrack(i):
    numTimes= [0]*7

    for b in range(i):
        numTimes[rand7()] += 1
    for b  in range(len(numTimes)):
        numTimes[b] = numTimes[b]/(i/100)
    return numTimes    
    
def recbackTrack(n, string = "", strings = []):
    if n == 0:
        pass
        #print(string)
    else:
        for c in ['a', 'b']:
            recbackTrack(n-1, string + c)
        
        
