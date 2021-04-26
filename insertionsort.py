def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        ## DO This loop for every item in the list
        key = sort_list[i] ##look at the first item in the list
                        ## but the next loop it will be the second item 
        j = i - 1


        ## run this loop at most i-1 times
        ## or until the key(current value) is
        ## less than the next value in the list
        while j >= 0 and key < sort_list[j]:
            ##if the key >= the previous item don't do anything
            ## because it is in the proper postition relative to the
            ## items before it

            ##otherwise move the value before the key down one position
            sort_list[j + 1] = sort_list[j]
            ## deincrement j
            j -= 1
        sort_list[j + 1] = key
    return sort_list
