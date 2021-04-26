def genMS(n, t):
    types = [n for n in range(t)]
    sets = ['X']*(n+t-1)
    return convertToMulti(addBreaks(sets, t-1))

def addBreaks(sets, t):
    if(t == 0):
        return [sets]    
    if(len(sets) == t):
        for i in range(len(sets)):
            sets[i] = 'O'
        return [sets]

    else:
        return ([['X'] + n for n in addBreaks(sets[1:], t)] +
    [['O'] + n for n in addBreaks(sets[1:],t - 1)])
    
    
def convertToMulti(sets):
    output = []
    for MS in sets:
        curr = 0
        newForm = []
        for item in MS:
            if item == 'X':
                newForm.append(curr)
            else:
                curr += 1
        output.append(newForm)
    return output


def countSetsContainingAll(sets):
    i = 0
    for item in sets:
        if(1 in item and 0 in item and 2 in item):
            i += 1
    return i

def countSetsEvenMultiplicity(sets, types):
    i = 0
    for item in sets:
        if(all([i % 2 == 0 for i in [item.count(t) for t in range(types)]])):
           i+=1
    return i

def countSetsOddMultiplicity(sets, types):
    i = 0
    for item in sets:
        if(all([i % 2 == 1 for i in [item.count(t) for t in range(types)]])):
           i+=1
    return i
                     
