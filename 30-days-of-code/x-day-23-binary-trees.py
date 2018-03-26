import itertools

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def zip_longest_nofill(self, *args):
        empty = object()
        its = [iter(arg) for arg in args]
        while True:
            vals = (next(it, empty) for it in its)
            tup = tuple(val for val in vals if val is not empty)
            if not tup:
                return
            yield tup

    def levelOrder(self,root):
        level = self.getLevel(root)
        level.insert(0,root.data)
        print(" ".join(str(num) for num in level))

    def getLevel(self,root):
        if root is None or root.data is None:
            return []

        level = []
        if root.left is not None:
            level.append(root.left.data)

        if root.right is not None:
            level.append(root.right.data)

        left = self.getLevel(root.left)
        right = self.getLevel(root.right)
        mix = list(itertools.chain.from_iterable(self.zip_longest_nofill(left, right)))
        print(left)
        print(right)
        return level + mix


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

