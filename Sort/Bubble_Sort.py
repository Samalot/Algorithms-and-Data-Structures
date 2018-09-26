def bubble_sort(d):

    for i in range( 1, len(d) ):
        
        swap = False
        for e in range( len(d) - i ):

            if d[e] > d[e+1]:
                swap = True
                d[e], d[e+1] = d[e+1], d[e]
                
        if not swap:
            return d
        
    return d



data = [2,4,1,7,3,5,9]
print( bubble_sort(data) )

