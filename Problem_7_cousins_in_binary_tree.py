"""
 Cousins in Binary tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
nodes = {}
def getLevel(node: TreeNode,parent,level: int):
        global nodes
        if node:
            nodes[node.val] = {'depth':level,'parent':parent}
            getLevel(node.left,node.val,level+1)
            getLevel(node.right,node.val,level+1)
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        getLevel(root,None,0)
        nodex = nodes[x]
        nodey = nodes[y]
        print(nodex['depth'] , nodey['depth'] , nodex['parent'], nodey['parent'])
        if nodex['depth'] == nodey['depth'] and nodex['parent'] != nodey['parent']:
            return True
        else:
            return False 
