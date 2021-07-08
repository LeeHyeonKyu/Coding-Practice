def height(root):
    if root :
        return find_depth(root) - 1
    else :
        return 0

def find_depth(node):
    l = r = 0
    if node.left :
        l = find_depth(node.left)
    if node.right :
        r = find_depth(node.right)
    return max(l, r) + 1
