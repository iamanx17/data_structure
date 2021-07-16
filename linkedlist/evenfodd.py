from linkedlist import takeinput, printdata

def reverse(head):
    tail=None
    while head is not None:
        nxt=head.next
        head.next=tail
        tail=head
        head=nxt
    return tail

def evenodd(head):
    even=None
    odd=None
    while head is not None:
        if head.data%2==0:
            nxt=head.next
            head.next=even
            even=head
            head=nxt
        else:
            nxt=head.next
            head.next=odd
            odd=head
            head=nxt
    odd=reverse(odd)
    even=reverse(even)
    source=odd
    while odd.next is not None:
        odd=odd.next
    odd.next=even
    return source  

head=takeinput()
printdata(head)
printdata(evenodd(head))