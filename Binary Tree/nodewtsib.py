from binarytree import takeinput, printdata

def nodeswtsib(root):
    if root is None:
        return 0
    count=0
    if root.left is None and root.right is None:
        count+=1
    
    left=nodeswtsib(root.left)
    right=nodeswtsib(root.right)
    return count+left+right

root=takeinput()
printdata(root)
print(nodeswtsib(root))