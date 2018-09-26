def merge(a, b):

    res = []
    i = j = 0
    for n in range(len(a)+len(b)):

        if a[i] < b[j]:
            res.append(a[i])
            i += 1
            if i >= len(a):
                return res + b[j:]

        else:
            res.append(b[j])
            j += 1
            if j >= len(b):
                return res + a[i:]
    
    return res


def merge_sort(data):

    if len(data) < 2:
        return data

    k = len(data) // 2
    a = merge_sort(data[:k])
    b = merge_sort(data[k:])
    
    return merge(a, b)




data = [ 3, 2, 83, 5, 7, 55, 4, 9, 8, 11, 2, 101, 1 ]

print( merge_sort(data) )
