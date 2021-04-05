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

for i in range(int(input())):
    head1=takeinput()
    printdata(head1)
    head2=takeinput()
    printdata(head2)
    res=mergesort(head1, head2)
    printdata(res)
  
