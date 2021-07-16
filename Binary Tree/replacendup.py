#replace node with its duplicate at left


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


def replacedup(root):
    if root is None:
        return
    if root.left is None:
        newroot=Node(root.data)
        root.left=newroot
    else:
        newroot=Node(root.data)
        temp=root.left
        root.left=newroot
        newroot.left=temp
        
    replacedup(root.left)
    replacedup(root.right)


root=takeinput()
printdata(root)

replacedup(root)
printdata(root)