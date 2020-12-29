# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root, ]
        sum = 0
        
        # 스택 이용 필요한 노드 DFS 반복
        while stack :
            node = stack.pop()
            if node :
                if node.val > low :
                    stack.append(node.left)
                if node.val < high :
                    stack.append(node.right)
                if low <= node.val <= high :
                    sum += node.val
        
        return sum

'''
Runtime : 204 ms
Memory : 22.2 MB
'''
