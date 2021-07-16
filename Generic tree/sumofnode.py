from GenericTree import takeinput, printdata

def sumofnode(root):
    if root is None:
        return 0    
    
    count=root.data
    for child in root.children:
        count+=sumofnode(child)
    return count
    

root=takeinput()
printdata(root)
print(sumofnode(root))

    
    
    
    
