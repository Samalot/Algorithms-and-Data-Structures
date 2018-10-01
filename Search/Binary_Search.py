from random import randint

def binarySearch(data, target, start, end):

    if start > end:
        return print(str(target) + " is not in the data")

    i = start + (end-start) // 2

    if data[i] == target:
        return print(str(target) + " is at position " + str(i))

    if data[i] > target:
        return binarySearch(data, target, start, i-1)
    
    return binarySearch(data, target, i+1, end)


### RUN
data = sorted([randint(0,100) for n in range(20)])
target = data[randint(0,19)]
print(data)
binarySearch(data, target, 0, 19)
binarySearch(data, 50, 0, 19)
