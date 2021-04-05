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

for i in range(int(input())):
    head=takeinput()
    printdata(head)
    head=reverse(head)
    printdata(head)
