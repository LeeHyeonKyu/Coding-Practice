# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root, ])
        result = ['#']
        
        # 트리 BFS 직렬화
        while queue :
            node = queue.popleft()
            if node :
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else : result.append('#')
        return ' '.join(result)
        
        

    def deserialize(self, data):
        # 예외 처리
        if data == '# #' :
            return None
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root, ])
        index = 2
        
        # 런너 기법과 유사하게 자식 노드 결과를 먼저 확인 후 큐에 삽입
        while queue :
            node = queue.popleft()
            if nodes[index] is not '#' :
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if nodes[index] is not '#' :
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        
        return root

    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''
Runtime : 104 ms
Memory : 18.8 MB
'''
