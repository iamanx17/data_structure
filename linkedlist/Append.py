#Append last n to first
from linkedlist import takeinput, printdata

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def append(head, n):
    count=0
    source=head
    while count<length(head)-n:
        curr=head
        head=head.next
    
    newhead=head
    while head.next is not None:
        head=head.next
    curr.next=None
    head.next=source
    return newhead



head=takeinput()
printdata(head)
n=int(input())
printdata(append(head, n))
