from linkedlist import takeinput, printdata

def kreverse(head, k):
    count=0
    prev=None
    while count<k:
        nxt=head.next
        head.next=prev
        prev=head
        head=nxt
        count+=1
    save=prev
    while prev.next is not None:
        prev=prev.next
    
    prev.next=head
    return save


head= takeinput()
printdata(head)
k=int(input())
printdata(kreverse(head, k))