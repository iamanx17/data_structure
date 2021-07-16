from Queue import Queue

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
    


def reversehelper(q,k,s):
    while s.size()!=1:
        ele=s.pop()
        q.enqueue(ele)
    last=s.pop()
    while q.size()<k:
        ele=q.dequeue()
        s.push(ele)        
    reversehelper(q,s)
    q.enqueue(last)
    return q

def reversek(q,k,s):
    count=0
    while count<k:
        ele=q.dequeue()
        s.push(ele)    
    reversehelper(q,s)


s=Stack()
q=Queue()
for i in range(1,6):
    q.enqueue(i)

print('top element is', q.front())

reversek(q,3,s)
print('top element is ', q.front())

