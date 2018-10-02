## Print function
def printTower(t):
    for n in range(3):
        if len(t[n]) > 1:
            for i in range(len(t[n])-1):
                if t[n][i] < t[n][i+1]:
                    print(str(t) + " = INVALID")
                    return
    print(str(t))



## Recursive solution
def hanoi(t, a, b, c, n):

    if n == 1:      
        t[b].append(t[a].pop())
        t[3] += 1
        printTower(t)
        return t

    t = hanoi(t, a, c, b, n-1)
    t[b].append(t[a].pop())
    t[3] += 1
    printTower(t)
    t = hanoi(t, c, b, a, n-1)
    
    return t


    
## RUN
n = 4
t = [[(n-i) for i in range(n)],[],[], 0]
hanoi(t, 0, 2, 1, n)

