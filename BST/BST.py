class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

class BST:
    def __init__(self):
        self.root=None
        self.count=0
    
    def inserthelper(self, root, data):
        if root is None:
            root=Node(data)
            return root
        
        newnode=Node(data)
        if data<root.data:
            root.left=inserthelper(root.left, data)
            return root

        if data>root.data:
            root.right=inserthelper(root.right, data)
            return root

    def insert(self, data):
        self.root=self.inserthelper(self.root,data)
        self.count+=1
    
    def printdatahelper(self, root):
        if root is None:
            return 
        print(root.data, end=':')
        if root.left is not None:
            print('L', root.left.data, end=',')
        if root.right is not None:
            print('R', root.right.data)
        print()

        printdatahelper(root.left)
        printdatahelper(root.right)    
    
    def printdata(self):
        self.printdatahelper(self.root)
    
    def ispresenthelper(self, root, data):
        if root is None:
            return False
        
        if root.data==data:
            return True

        left=ispresenthelper(root.left, data)
        if left:
            return True
        
        right=ispresenthelper(root.right, data)
        return False
    
    def ispresent(self, data):
        self.ispresenthelper(self.root, data)
    
    def size(self):
        return self.count
    

    def delete(self, data):
        #doubt
        