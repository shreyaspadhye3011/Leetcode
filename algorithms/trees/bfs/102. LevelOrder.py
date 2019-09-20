# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Approach: BFS modified to store every node's children, depth by depth. Add logic to keep track of depth of retrieved parent by keeping a dictionary and update depth by 1 while making subsequent calls

#TODO: Add logic to keep track of depth of retrieved parent by keeping a dictionary and update depth by 1 while making subsequent calls
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    def getChildren(self):
        # update to facilitate for graphs. Currently made for trees. For graphs, it will be done through adjacency list
        if self.left and self.right:
            return [self.left, self.right]
        elif self.left:
            return [self.left]
        elif self.right:
            return [self.right]
        else:
            return None


class Solution():
    def levelOrder(self, root):
        access = [root]
        result = []
        while(len(access) > 0):
            node = access.pop(0)
            childList = node.getChildren()
            if childList:
                result.append(childList)
            for child in childList:
                access.append(child)
        return result

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

root = Node(1)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
# root.PrintTree()
# root.breadthFirstSearch()

obj = Solution()
obj.levelOrder(root)
