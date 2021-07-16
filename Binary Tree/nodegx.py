#Node greater than x
from binarytree import takeinput, printdata

def nodegtx(root, x):
    if root is None:
        return 
    count=0
    if root.data>x:
        count+=1
        return count
    
    left=nodegtx(root.left,x)
    right=nodegtx(root.right,x)

    return count+left +right


root=takeinput()
printdata(root)
x=int(input())
print(nodegtx(root,x))
