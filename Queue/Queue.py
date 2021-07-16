#Queue follows last in first out method
# insertion take place at tail
# deletion take place at head
# enqueue, dequeue, count, front, isEmpty

#Can be implemented as array and linkedlist

#we will implement as linked list



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class Queue:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    
    def enqueue(self, data):
        newnode=Node(data)
        if self.__head is None:
            self.__head=newnode
            self.__tail=newnode
        else:
            self.__tail.next=newnode
            self.__tail=newnode
        self.__count+=1
    
    def dequeue(self):
        if self.isEmpty():
            return 0
        
        data=self.__head.data
        self.__head = self.__head.next
        self.__count-=1
        return data
    
    def printdata(self):
        while self.__head is not None:
            print(self.__head.data, end='->')
            self.__head=self.__head.next
        print('None')
        
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size()==0
    
    def front(self):
        if self.isEmpty():
            return 0
        data=self.__head.data
        return data
    

