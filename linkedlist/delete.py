from linkedlist import takeinput, printdata

def delete(head, i):
    count=0
    source=head
    while count<i:
        curr=head
        head=head.next
        count+=1
    curr.next=head.next
    return source

head=takeinput()
printdata(head)
i=int(input())
printdata(delete(head, i))