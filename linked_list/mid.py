from Node import *

def mid(head):
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    
    return slow

for i in range(int(input())):
    head=takeinput()
    print(mid(head).data)