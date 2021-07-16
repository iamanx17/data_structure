class Node:
    def __init__(self,data):
        self.data=data
        self.children=list()
    

def takeinput():
    data=int(input())
    if data == -1:
        return 
    
    root=Node(data)
    print('Enter the children of', root.data)
    for i in range(int(input())):
        child=takeinput()
        root.children.append(child)
    return root

def printdata(root):
    if root is None:
        return
    
    print(root.data, end=':')
    for child in root.children:
        print(child.data, end=',')
    print()

    for child in root.children:
        printdata(child)

