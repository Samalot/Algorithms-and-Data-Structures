def eratosthenes(limit):

    n = [True] * limit
    n[0] = n[1] = False 
    primes = [2]

    for i in range(2,limit):
        
        if n[i]:
            primes.append(i+1)
            n[i] = False
            
            for j in range(i+(i+1) ,limit, i+1):
                n[j] = False

    print(primes)
    return primes


### RUN
eratosthenes(100)
