def day82(rem, mapping, strings=[]):
    if len(rem) == 1:
        newstrings = strings*len(mapping[rem[0]])
        i = 0
        for item in mapping[rem[0]]:
            b = 0
            while b < len(newstrings)/len(mapping[rem[0]]):
                newstrings[i] = newstrings[i] + item
                b = b + 1
                i = i + 1
        print(newstrings)
    else:

        if len(strings) == 0:
            newstrings = [None]*3
            i = 0
            for item in mapping[rem[0]]:
               
                newstrings[i] = item
                i = i+1
        else:
            newstrings = strings*len(mapping[rem[0]])
            i = 0
            for item in mapping[rem[0]]:
                b = 0
                while b < len(newstrings)/len(mapping[rem[0]]):
                    newstrings[i] = newstrings[i] + item
                    b = b + 1
                    i = i + 1
        del rem[0]

        day82(rem, mapping, newstrings)
