class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    

def takeinput():
    data=int(input())
    if data==-1:
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
        print('L', root.left.data , end=',' )
    if root.right is not None:
        print('R', root.right.data)
    print()

    printdata(root.left)
    printdata(root.right)