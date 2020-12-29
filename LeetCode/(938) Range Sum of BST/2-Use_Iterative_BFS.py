# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue = collections.deque([root, ])
        sum = 0
        
        # 큐 이용 필요한 노드 BFS 반복
        while queue :
            node = queue.popleft()
            if node :
                if node.val > low :
                    queue.append(node.left)
                if node.val < high :
                    queue.append(node.right)
                if low <= node.val <= high :
                    sum += node.val
        
        return sum

'''
Runtime : 196 ms
Memory : 22.5 MB
'''
