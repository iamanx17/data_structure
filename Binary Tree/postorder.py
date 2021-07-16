#postorder means leftchild, rightchild root

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

def postorder(root):
    if root is None:
        return 
    
    postorder(root.left)
    postorder(root.right)

    print(root.data, end=' ')


root=takeinput()
postorder(root)