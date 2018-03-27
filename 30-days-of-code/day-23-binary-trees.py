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

    def visit(self, root):
        child_list = []

        if root.left is not None:
            child_list.append(root.left)
        if root.right is not None:
            child_list.append(root.right)
        return child_list

    def levelOrder(self, root):
        if root is None:
            return

        level = [root]
        queue = [root]
        while len(queue):
            visit = self.visit(queue[0])
            queue.pop(0)
            queue += visit
            level += visit

        print(" ".join(str(num.data) for num in level))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

