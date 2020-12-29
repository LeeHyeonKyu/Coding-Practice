# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node) :
            if not node :
                return 0
            
            # 가지치기 후 재귀 호출
            if node.val < low :
                return dfs(node.right)
            elif node.val > high :
                return dfs(node.left)
            else :
                return node.val + dfs(node.right) + dfs(node.left)
            pass # end dfs
        
        return dfs(root)

'''
Runtime : 200 ms
Memory : 22.4 MB
'''
