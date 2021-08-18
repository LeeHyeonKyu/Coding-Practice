from collections import defaultdict

class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.nodes = defaultdict(str)

def str_to_node(char):
    if char not in tree.nodes:
        node = Node(char)
        tree.nodes[char] = node
    else:
        node = tree.nodes[char]
    return node

tree = Tree()
N = int(input())
for i in range(N):
    P, L, R =  input().split()
    p_node = str_to_node(P)
    l_node = str_to_node(L)
    r_node = str_to_node(R)
    p_node.left = l_node
    p_node_right = r_node

def preorder(node, lst):
    if node.name == '.':
        pass
    else:
        lst.append(node.name)
        if node.left is not None:
            preorder(node.left, lst)
        if node.right is not None:
            preorder(node.right, lst)
    return ''.join(lst)

def inorder(node, lst):
    if node.name == '.':
        pass
    else:
        if node.left is not None:
            inorder(node.left, lst)
        lst.append(node.name)
        if node.right is not None:
            inorder(node.right, lst)
    return ''.join(lst)

def postorder(node, lst):
    if node.name == '.':
        pass
    else:
        if node.left is not None:
            postorder(node.left, lst)
        if node.right is not None:
            postorder(node.right, lst)
        lst.append(node.name)
    return ''.join(lst)

print('')
print(preorder(tree.nodes['A'], []))
print(inorder(tree.nodes['A'], []))
print(postorder(tree.nodes['A'], []))