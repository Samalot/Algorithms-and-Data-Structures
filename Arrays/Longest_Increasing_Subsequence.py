def LIS(a):
    l = [ [] for i in range(len(a)) ]
    l[0] = [a[0]]

    for i in range(1, len(a)):
        for j in range(i):
            if (a[j] < a[i]) and (len(l[i]) < len(l[j])):
                l[i] = l[j][:]
        l[i].append(a[i])
        
    maxL = []
    for sequence in l:
        if len(sequence) > len(maxL):
            maxL = sequence

    print(maxL)
    return maxL



### RUN
data = [3,2,6,4,5,1]
LIS(data)
