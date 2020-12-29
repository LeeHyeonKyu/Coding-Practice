# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node) :
            # 종료 조건
            if node is None :
                return 0
            
            # 리프 노드까지 DFS 재귀 탐색
            if node.left :
                l = dfs(node.left)
            if node.right :
                r = dfs(node.right)
            
            # 값 비교 후 거리 추가 or 초기화
            if node.left and node.left.val == node.val :
                l += 1
            else :
                l = 0
            if node.right and node.right.val == node.val :
                r += 1
            else :
                r = 0
            
            # 최대 거리 갱신
            self.result = max(self.result, l + r)
            # 부모 노드엔 더 긴 쪽을 return
            return max(l, r) # end dfs
        
        dfs(root)
        return self.result

'''
Runtime : 392 ms
Memory : 18 MB
'''
