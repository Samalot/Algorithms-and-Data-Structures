def job_schedule(events):

    events.sort()
    scores = [e[2] for e in events]
    path = [None for e in events]

    for i in range(1,len(events)):
        for j in range(i):
            if events[i][1] >= events[j][0]:
                f = scores[j] + events[i][2]
                if f > scores[i]:
                    scores[i] = f
                    path[i] = j

    # Find max result    
    maxIndex = 0
    maxScore = 0
    for i in range(len(scores)):
        if scores[i] > maxScore:
            maxScore = scores[i]
            maxIndex = i

    # Traceback result
    res = [events[maxIndex]]
    maxIndex = path[maxIndex]
    while not maxIndex == None:
        res.append(events[maxIndex])
        maxIndex = path[maxIndex]
    print(res)

    return res



## Data
## (F, S, W)
## F - Finish time
## S - Start time
## W - Weight

events = [[3,1,5],
          [5,2,6],
          [6,4,5],
          [7,6,4],
          [9,7,2],
          [8,5,11]]

job_schedule(events)
