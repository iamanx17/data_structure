from linkedlist import takeinput, printdata

def mergesort(head1, head2):
    if head1 is None:
        return None
    if head2 is None:
        return None
    if head1.data <= head2.data:
        head=head1
        tail=head1
        head1=head1.next
    else:
        head=head2
        tail=head2
        head2=head2.next
    
    while head1 is not None and head2 is not None:
        if head1.data>=head2.data:
            tail.next=head2
            tail=head2
            head2=head2.next
        else:
            tail.next=head1
            tail=head1
            head1=head1.next
    
    if head1 is None:
        tail.next=head2
    if head2 is None:
        tail.next=head1
    
    return head


head1=takeinput()
head2=takeinput()
printdata(head1)
printdata(head2)
printdata(mergesort(head1, head2))