# stack using linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stackusingll:
    def __init__(self):
        self.__head=None
        self.__size=0
    
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.__head
        self.__head=newnode
        self.__size+=1

    def pop(self):
        if self.isEmpty() is True:
            return 0
        data=self.__head.data
        self.__head=self.__head.next
        self.__size=self.__size-1
        return data
    
    def top(self):
        if self.isEmpty() is True:
            return 0
        data=self.__head.data
        return data
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size()==0 

