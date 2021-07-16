from linkedlist import takeinput, printdata

def duplicate(head):
    source=head
    while head.next is not None:
        if head.data==head.next.data:
            head.next=head.next.next
        head=head.next
    return source

head=takeinput()
printdata(head)
printdata(duplicate(head))