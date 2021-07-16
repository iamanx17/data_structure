from binarytree import takeinput,printdata

def sumofnode(root):
    if root is None:
        return 0
    
    left=sumofnode(root.left)
    right=sumofnode(root.right)
    return root.data + left + right


root=takeinput()
printdata(root)
print(sumofnode(root))