from linkedlist import takeinput, printdata


def reverse(head):
    tail=None
    while head is not None:
        nxt=head.next
        head.next=tail
        tail=head
        head=nxt
    return tail


head=takeinput()
printdata(head)
printdata(reverse(head))