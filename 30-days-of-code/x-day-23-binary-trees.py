import sys

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

    def levelOrder(self,root):
        print(str(root.data) + " " + self.getLevel(root))

    def getLevel(self,root):
        if root is None or root.data is None:
            return ""

        level = ""
        if root.left is not None:
            level += str(root.left.data) + " "

        if root.right is not None:
            level += str(root.right.data) + " "

        level += self.getLevel(root.left)
        level += self.getLevel(root.right)

        return level


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

