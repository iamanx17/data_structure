from Queue import Queue
#reverse queue using stack or queue

def reverse(q):
    s=[]
    while q.size()!=0:
        s.append(q.dequeue())    

    for i in range(len(s)):
        q.enqueue(s.pop())
    return q


q=Queue()
for i in range(1, 6):
    q.enqueue(i)
print('Top element is ', q.front())


reverse(q)
print('Now top element is ', q.front())


