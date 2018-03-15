class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

def hasChild(node_obj):
    return node_obj.left is not None or node_obj.right is not None


def checkBST(root):
    while hasChild(root):
        pass

print(checkBST(root))