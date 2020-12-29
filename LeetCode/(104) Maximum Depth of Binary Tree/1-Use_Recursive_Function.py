# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def count_depth(node, depth) :
            l = r = depth
            if node is None :
                return depth
            if node.left :
                l = count_depth(node.left, depth+1)
            if node.right :
                r = count_depth(node.right, depth+1)
            return max(l, r)
        
        if root is None : 
            return 0
        else : 
            return count_depth(root, 1)

'''
Runtime : 36 ms
Memory : 16.4 MB
'''
