class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def takeinput():
    rootdata=int(input())
    if rootdata == -1:
        return None

    root=Tree(rootdata)
    leftree=takeinput()
    rightree=takeinput()
    root.left=leftree
    root.right=rightree
    return root

def numnode(root):
    if root==None:
        return 0
    leftcount = numnode(root.left)
    rightcount = numnode(root.right)
    return 1 + leftcount + rightcount

def leaf(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    numleft=leaf(root.left)  
    numright=leaf(root.right)
    return numleft+numright


def maximum(root):
    if root==None:
        return -1
    
    leftlarg=maximum(root.left)
    rightlarg=maximum(root.right)
    largest=max(leftlarg,rightlarg,root.data)
    return largest

def printree(root):
    if root is None:
        return
    print(root.data,end=':')
    if root.left is not None:
        print('L',root.left.data,end=',')
    else:
        print('L','None',end=',')
    if root.right is not None:
        print('R',root.right.data)
    else:
        print('R','None')
    printree(root.left)
    printree(root.right)

root=takeinput()
printree(root)
print(maximum(root))
