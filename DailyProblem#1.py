def canSum(nums, k):
    length = len(nums)-1
    for i in range(len(nums)):
        j = length
        while j > i:
            
            print(nums[i] + nums[j])
            if nums[i]+nums[j] == k:
                return True
            j = j - 1
    return False

#day number dos
def newSumArray(arr):
    temp = 1
    stor = [0]*len(arr)
    for number in arr:
        temp = temp * number

    for i in range(len(arr)):
        stor[i] = temp//arr[i]
    return stor

def day4(array):
   
    array.sort()
    i = 0
    while i < len(array):
        if array[i] <= 0:
            del array[i]
        else:
            i = i + 1
    length = len(array)
    for i in range(length):
        if array[i] != i+1:
            return i+1
    return length + 1
def day52(string, k, result = []):
    first = False
    length = 0
    result.append([])
    
    for i in range(len(string)):
        if first:
            length = length + 1
        if len(string[i]) + length < k:
            result[-1].append(string[i])
            length = length + len(string[i])
            first = True
        else:
            for b in range(i):
                string.remove(string[0])
            break
    day52(string, k , result)
def day58(array, num):
    length = len(array)
    pos1 = length//4
    pos2 = length*3//4
    a = array[pos1]
    if a == num:
        return pos1
    b = array[pos2]
    if b == num:
        return pos2
    if num > a and num < b:
        day58(array[pos1:pos2], num)
    else:
        day58(array[-pos1:pos1], num)



    
