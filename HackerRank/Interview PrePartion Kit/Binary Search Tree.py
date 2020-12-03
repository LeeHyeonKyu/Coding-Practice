def lca(root, v1, v2):
    n = root
    while n is not None :
        if n.info > v1 and n.info > v2 :
            n = n.left
        elif n.info < v1 and n.info < v2 :
            n = n.rigth
        else :
            break
    return n
