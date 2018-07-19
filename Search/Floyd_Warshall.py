def floyd_warshall (n, edges):

    ## Initialise the distance matrix.
    d = [ [ 0 if x == y else 1000 for x in range(n) ] for y in range(n) ]
    
    for e in edges:
        d[e[0]][e[1]] = e[2]

    ## Main Loop
    for i in range(n):
        for y in range(n):
            for x in range(n):
                                   
                    if d[i][x] + d[y][i] < d[y][x]:
                            d[y][x] = d[i][x] + d[y][i]

    return d


## Number of nodes and Edges (with weight) - Edges are directed.
n = 8
edges = [[0,1,10],
         [0,2,1],
         [2,1,5],
         [1,3,4],
         [2,4,18],
         [3,4,2],
         [3,5,20],
         [4,5,2],
         [2,6,100],
         [6,4,0],
         [2,7,1],
         [7,4,29]]

## Run
for r in floyd_warshall(n, edges):
    print(r)

