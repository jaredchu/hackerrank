""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root):
    if(isBST(root,root.left.data,root.right.data)):
        print('Yes')
    else:
        print('No')

def isBST(root, left, right):
    if (root is None):
        return False
    if ((left is not None and root.data <= left) or (right is not None and root.data >= right)):
        return False
    return isBST(root.left, root.left.left, root.right.right) and isBST(root.right, root.left.left, root.right.right)

root = node(2)
root.left = node(1)
root.right = node(3)

checkBST(root)