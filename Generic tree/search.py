from GenericTree import takeinput, printdata

def search(root, x):
    if root is None:
        return False
    
    if root.data==x:
        return True
    
    for child in root.children:
        if search(child, x):
            return True
    return False
    

root=takeinput()
printdata(root)
x=int(input())
print(search(root,x))