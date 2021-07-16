#replace node with depth

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
def takeinput():
    data=int(input())
    if data == -1:
        return 
    root=Node(data)
    root.left=takeinput()
    root.right=takeinput()
    return root

def printdata(root):
    if root is None:
        return 
    print(root.data, end=':')
    if root.left is not None:
        print(root.left.data, end=',')
    if root.right is not None:
        print(root.right.data)
    print()
    printdata(root.left)
    printdata(root.right)

def replacenode(root, level):
    if root is None:
        return 
    
    root.data=level
    replacenode(root.left, level+1)
    replacenode(root.right, level+1)

root=takeinput()
replacenode(root,0)
printdata(root)