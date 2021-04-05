from Node import *

def mergesort(head1,head2):
    fhead=None
    ftail=None
    if head1.data<=head2.data:
        fhead=head1
        ftail=head1
        head1=head1.next
    else:
        fhead=head2
        ftail=head2
        head2=head2.next
    
    while head1 is not None and head2 is not None:
        if head1.data>=head2.data:
            ftail.next=head2
            ftail=ftail.next
            head2=head2.next
       
        else:
            ftail.next=head1
            ftail=ftail.next
            head1=head1.next    

    if head1 is None:
        ftail.next=head2
    if head2 is None:
        ftail.next=head1
        
        
    return fhead

def mid(head):
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow
    

def merge(head):
    left=head
    middle=mid(left)
    nextomid=middle.next
    middle.next=None
    res=mergesort(left,nextomid)
    return res  


for i in range(int(input())):
    head=takeinput()
    res=merge(head)

    printdata(res)
   


    

