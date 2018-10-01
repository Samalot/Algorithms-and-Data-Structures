def kadane(data):

    max_global, max_local = data[0], data[0]

    for i in range(1, len(data)):

        max_local = max( data[i], data[i] + max_local )
        
        if max_local > max_global:
            max_global = max_local
        
    return max_global

## Run
d = [1,2,3,4,-100,-2,-3,2,3,4,5,-9,4,5]

print(kadane(d))
