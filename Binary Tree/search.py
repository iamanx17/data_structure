from binarytree import takeinput, printdata

def search(root, x):
    if root is None:
        return False
    
    if root.data==x:
        return True
    
    left=search(root.left,x)
    if left:
        return True
    right=search(root.right,x)
    return right

root=takeinput()
printdata(root)
x=int(input())
print(search(root, x))