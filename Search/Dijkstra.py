from heapq import heappush
from heapq import heappop

def dijkstras(n, edges, s, d):

    # Set up the edge hash for convenience
    e = {p: [] for p in range(n) }
    for edge in edges:
        e[edge[0]].append(edge)

    # Set the distance of the edges to infinite and source to 0
    dist = { p: 10**100 for p in range(n) }
    dist[s] = 0

    # Set up
    seen = set()
    h = [(0,s)]

    ## Main loop
    while len(h) > 0:
        current = heappop(h)

        # Check each outgoing edge from current
        for neighbour in e[current[1]]:
            if not neighbour[1] in seen:
                
                t = dist[current[1]] + neighbour[2]
                
                if t < dist[neighbour[1]]:
                    
                    dist[neighbour[1]] = t
                    heappush(h, (t, neighbour[1]))
            
        # Mark current node as seen   
        seen.add(current[1])
         
    return dist[d]

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

## Source and Destination
s = 0
d = 5

## Run
res = dijkstras(n, edges, s, d)
print(res)
