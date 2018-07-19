import heapq

def codebook(data):

    ## Create a frequency heap
    freq = {}
    for c in data:
        freq[c] = freq.get(c, 0) + 1

    ## Create a heap from the frequencies (inverted values to it becomes a max heap)
    heap = [ (freq[c], c) for c in freq ]
    heapq.heapify(heap)

    ## Construct a binary tree using the heap.
    tree = {}
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        tree[a[1]] = ( 0, a[1]+b[1] )
        tree[b[1]] = ( 1, a[1]+b[1] )
        
        heapq.heappush( heap, ( a[0]+b[0], a[1]+b[1] ) )

    ## Build the codebook by tracing the tree for each char.
    codebook = {}
    for c in freq:

        code = ""
        pointer = c
        while pointer in tree:
            code = str(tree[pointer][0]) + code
            pointer = tree[pointer][1]

        codebook[c] = code

    return codebook


def encode( codebook, data ):

    ## Encode original data (In a real application you'd use some kind of stream)
    encoded_bits = ""
    for c in data:
        encoded_bits += codebook[c]

    fill_bits = 7 - (len(encoded_bits) % 7 )
    encoded_bits += "0" * fill_bits

    encoded_data = ""
    for i in range(len(encoded_bits) // 7):
        encoded_data += int( encoded_bits[i*7:(i*7)+7] , 2).to_bytes(1, 'big').decode()

    return encoded_data


def decode ( codebook, data ):

    ## Reverse codebook
    codebook = { codebook[c]:c for c in codebook }

    full_data = ""
    for c in data:
        full_data += bin(int.from_bytes(c.encode(), 'big'))[2:].zfill(7)

    decoded_data = ""
    buffer = ""
    for c in full_data:
        
        buffer += c
        if buffer in codebook:

            decoded_data += codebook[buffer]
            buffer = ""

    return decoded_data


## Data
data = "the dog ran over the road to catch the cat, the cat ran away from the dog and escaped"

## Run
codebook = codebook(data)
encoded_data = encode(codebook, data)
decoed_data = decode(codebook, encoded_data)

## Results
print("Original data = " + data)
print("Size of = " + str(len(data)) + "\n")

print("Encoded data = " + encoded_data)
print("Size of = " + str(len(encoded_data)) + "\n")

print("Decoded data = " + decoed_data)
print("Size of = " + str(len(decoed_data)) + "\n")
