from Queue import Queue

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None    

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
    
    def push(self, data):
        self.q1.enqueue(data)
    
    def pop(self):
        while self.q1.size()!=1:
            ele=self.q1.dequeue()
            self.q2.enqueue(ele)
        last=self.q1.dequeue()

        while self.q2.size()!=0:
            ele=self.q2.dequeue()
            self.q1.enqueue(ele)
        return last

    def size(self):
        return self.q1.size()
    
    def top(self):
        while self.q1.size()!=1:
            ele=self.q1.dequeue()
            self.q2.enqueue(ele)
        last=self.q1.front()
        while self.q2.size()!=0:
            ele=self.q2.dequeue()
            self.q1.enqueue(ele)        
        return last
    
    def isEmpty(self):
        return self.size()==0
    

s=Stack()
for i in range(1,10):
    s.push(i)

print('top element is',s.top())
print('stack is ',s.isEmpty())
print('stack size is',s.size())
for i in range(s.size()):
    print(s.pop())
