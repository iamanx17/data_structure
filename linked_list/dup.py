from Node import *

def duplicate(head):
    source=head
    while head.next is not None:
        curr=head.next
        if head.data == curr.data:
            head.next=curr.next
        else:
            head=head.next
    return source


for i in range(int(input())):
    head=takeinput()
    printdata(duplicate(head))
        
        