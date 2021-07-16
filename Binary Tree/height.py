from binarytree import takeinput, printdata

def height(root):
    if root is None:
        return
    
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1
    

root=takeinput()
printdata()
print(height(root))