## Greedy Algorithm for Set Cover.
def set_cover_greedy(U, S, C):

    res = []
    I = set([])
    maxCost = sum(C)

    while(not I == U):

        if len(S) == 0:
            return False

        minRatio = maxCost
        minSet = -1
        toRemove = []
        for i in range(len(S)):

            diff = len(S[i] - I)
            if diff > 0:
                ratio = C[i] / len(S[i] - I)
                if ( ratio ) < minRatio:
                    minRatio = ratio
                    minSet = i
            else:
                toRemove.append(i)

        if minSet >= -1:
            I.update(S[minSet])
            res.append(S[minSet])
            del(S[minSet])

        for i in toRemove:
            del(S[i])
        
    return res


## RUN
U = set([1,2,3,4,5])

S = [ set([4,1,3]),
      set([2,5]),
      set([1,4,3,2]) ]

C = [5, 10, 3]

print( set_cover_greedy(U, S, C) )
