## Hashing Functions
def ord_hash(key):
    total = 0
    for i in range(len(key)):
        total += ord(key[i]) * (31**i)
    return total

def djb2_hash(key):
    hash = 5381
    for s in key:
        hash = (( hash << 5 ) + hash ) + ord(s)
    return hash & 0xFFFFFFFF

def sdbm_hash(key):
    hash = 0;
    for c in key:
        hash = ord(c) + (hash << 6) + (hash << 16) - hash;
    return hash

## Main Code
class Bloom_Filter:

    def __init__(self, n):
        self.filter = [ 0 for i in range(n) ]

    def hash_key(self, key, n):
        h1 = ord_hash(key)
        h2 = djb2_hash(key)
        h3 = sdbm_hash(key)
        return [ h1 % n, h2 % n, h3 % n ]

    def add(self, key):
        print("Adding " + key + " to the set")
        for i in self.hash_key(key, len(self.filter)):
            self.filter[i] = 1

    def check(self, key):
        for i in self.hash_key(key, len(self.filter)):
            if self.filter[i] == 0:
                print(key + " is NOT in the set")
                return
        print(key + " MIGHT be in the set")
            
            
## Run
bf = Bloom_Filter(250)

bf.check("dog")

bf.add("dog")
bf.add("frog")
bf.add("cat")
bf.add("pie")

bf.check("dog")
bf.check("house")
bf.check("apple")
bf.check("frog")

