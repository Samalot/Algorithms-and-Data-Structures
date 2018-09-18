from random import randint

## Keep shuffling the data until it is in order.
def bogo_sort(data):
    while (not is_sorted(data)):
        data = shuffle(data)
    return data

## Are the elements in ascending order?
def is_sorted(data):
    for i in range(len(data)-1):
        if data[i+1] < data[i]:
            return False
    return True

## Randomly shuffle the elements.
def shuffle(data):
    for i in range(len(data)):
        j = randint(0, len(data)-1)
        data[i], data[j] = data[j], data[i] 
    return data


## RUN
data = [ randint(0, 100) for i in range(10) ]
print(data)

sortedData = bogo_sort(data)
print(sortedData)
