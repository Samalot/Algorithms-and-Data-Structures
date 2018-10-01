####################################################################
##                                                                ##
##  Given a tree, return the number of non-empty Unival subtrees  ##
##  - trees where the values all contained nodes are the same     ##
##                                                                ##
####################################################################

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival(node):
    
    if not (node.left or node.right):
        return [1,True]

    count = 0
    is_unival = True

    if node.left:
        l = count_unival(node.left)
        count += l[0]
        is_unival &= ( l[1] and node.val == node.left.val )

    if node.right:
        r = count_unival(node.right)
        count += r[0]
        is_unival &= ( r[1] and node.val == node.right.val )

    if is_unival:
        count += 1

    return [count, is_unival]





### RUN
root = Node(3)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(2)
root.right.right.left = Node(2)
root.right.right.right = Node(2)

print(count_unival(root)[0])
