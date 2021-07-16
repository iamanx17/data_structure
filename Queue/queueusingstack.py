#needs some improvement in code Fixing it soon....

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Stack:
    def __init__(self):
        self.__head=None
        self.__size=0
    
    def push(self, data):
        newnode=Node(data)
        newnode.next=self.__head
        self.__head=newnode
        self.__size+=1
    
    def top(self):
        if self.isEmpty():
            return 0
        
        data=self.__head.data
        return data

    def pop(self):
        if self.isEmpty():
            return 0
        
        data=self.__head.data
        self.__head=self.__head.next
        self.__size-=1
        return data
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size()==0
s1=Stack()
s2=Stack()    

class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        while self.s1.size()!=1:
            ele=self.s1.pop()
            self.s2.push(ele)
        last=self.s1.pop()        
        while self.s2.size()!=0:
            ele=self.s2.pop()
            self.s1.push(ele)        
        return last
    
    def size(self):
        return self.s1.size()
    
    def isEmpty(self):
        return self.size()==0
    
    def front(self):
        while self.s1.size()!=1:
            ele=self.s1.pop()
            self.s2.push(ele)
        
        top=self.s1.top()
        while self.s2.size()!=0:
            ele=self.s2.pop()
            self.s1.push(ele)
        return top


q=Queue

q.size()
q.isEmpty()
q.front()
for i in range(q.size()):
    print(q.dequeue())

