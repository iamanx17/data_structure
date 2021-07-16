#stack follows first in first out method
#insertion will be on head
#deletion will be on head
#can be implemented by using array and linked list
#push, pop, isEmpty, size, top

#here we will use linked list

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
    
