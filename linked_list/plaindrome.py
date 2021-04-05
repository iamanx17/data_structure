from Node import *

def reverse(head):
    prev=None
    curr=head
    while curr.next is not None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def plaindrome(head):
    if head is None:
        return True
    revhead=reverse(head)
    res=0
    while head.next is not None and revhead.next is not None:
        if head.data==revhead.data:
            pass
        else:
            res+=1    
    if res>0:
        return False
    else:
        return True
        

for i in range(int(input())):
    head=takeinput()
    print(plaindrome(head))