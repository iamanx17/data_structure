#preorder binary tree is Root leftchild rightchild
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


def preorder(root):
    if root is not None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.data)


root=takeinput()
preorder(root)
