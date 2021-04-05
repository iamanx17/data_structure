from Node import *


def reverse(head):
    prev=None
    curr=head
    while curr is not None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def evenodd(head):
    odd=None
    even=None
    curr=head
    while curr is not None:
        nxt=curr.next        
        if curr.data%2==0:
            curr.next=even
            even=curr
        else:
            curr.next=odd
            odd=curr
        curr=nxt

    evenre=reverse(even)
    head=reverse(odd)
    oddre=reverse(odd)
    while oddre is not None:
        if oddre.next is None:
            tail=oddre
        oddre=oddre.next
    tail.next=evenre
    return head

for i in range(int(input())):
    head=takeinput()
    res=evenodd(head)
    printdata(res)





            
        






for i in range(int(input())):
    head=takeinput()
    evenodd(head)